# Notes — M5: networking & the web

You type a name, hit Enter, and a page from a computer on the other side of the planet appears in under a second. This module traces *exactly* what happens in those moments — the address lookup (**DNS**), the **request and response**, the padlock (**HTTPS**), and why it's all so fast (**CDNs**). By the end, the web isn't magic — it's a sequence you can name.



## Internet vs web — not the same thing
People say them interchangeably, but:
- The **internet** is the global *network of networks* — the roads. (M1's "data center → cloud" computers, all wired together.)
- The **web** is *one thing that runs on* the internet: websites and pages. Email, video calls, app updates, and game servers also ride the same internet — the web is just the most visible passenger.

## Every device has an address: the IP
For a message to reach the right computer, each one needs a unique **IP address** — like `172.66.147.243`. The classic style (IPv4) is four numbers; a newer style (IPv6) is much longer and far more plentiful. Without an address, a reply has nowhere to go.

## DNS — the internet's phone book
You don't memorize `172.66.147.243`; you type `example.com`. The system that turns the *name* into the *number* is **DNS** (Domain Name System). Every time you open a site, your computer quietly asks DNS "what's the IP for this name?" first. (You'll do that lookup by hand in the lab with `dig`.)

## Client & server: request → response
Opening a page is a quick conversation:

```mermaid
sequenceDiagram
  participant C as You — the client
  participant S as Website — the server
  C->>S: Request - please send me this page
  S-->>C: Response - 200 OK + the page
```

Your device is the **client** — it sends a **request**. A **server** (a computer whose job is to serve pages) sends back a **response**, starting with a status like **`200`** (success). That request→response loop is the heartbeat of the web, and **HTTP** is the language they speak.

## HTTPS & TLS — what the padlock means
Plain **HTTP** is like a postcard: anyone who handles it along the way can read it. **HTTPS** is HTTP wrapped in **TLS encryption** — it scrambles the connection so only you and the server can read it. The **padlock** in your address bar means HTTPS is on.

How does your browser know the server is *really* `example.com` and not an impostor? A trusted authority issues the site a **TLS certificate** — a verifiable ID card. Your browser checks it automatically; you can inspect it yourself (who it's for, who issued it, and its valid dates). Modern reality: **HTTPS is now everywhere**, and browsers warn loudly on plain HTTP.

## How it physically travels: packets & routers
Your request isn't sent as one lump — it's broken into small **packets**. **Routers** forward each packet hop by hop across networks until it arrives, where they're reassembled. (Same idea whether it's across the room or across an ocean.)

## CDNs & the cloud — why it's fast and global
A big website isn't one computer in one place. It's copies cached on many servers worldwide — a **CDN** (content delivery network) — so you connect to a *nearby* one instead of a distant origin. That's why a site loads quickly whether you're in Lagos or London. Real example: `example.com` is actually served by **Cloudflare**, a CDN — you'll see "server: cloudflare" in the lab. This is "the cloud" doing its job (much more in M8).

## Ports — many services, one computer
A **port** is a numbered "door" a program listens at. The web uses **port 80** for HTTP and **port 443** for HTTPS. One server can run many services at once by listening on different ports.

## The whole trip, end to end
```mermaid
flowchart LR
  U["You type example.com"] --> DNS["DNS turns the name into an IP address"]
  DNS --> REQ["Your browser (client) sends an HTTPS request to that IP"]
  REQ --> CDN["A nearby CDN / cloud server receives it"]
  CDN --> RESP["Server replies: 200 + the page,<br/>encrypted by TLS (the padlock)"]
  RESP --> U
```

That entire chain runs every time you open a website — usually faster than you can blink.

## See it yourself
In your Codespace: `dig example.com` (watch the name become an IP), then `curl -I https://example.com` (see the `200` response come back over HTTPS). In a browser, click the **padlock** to read the site's certificate.

<details>
<summary><b>Go deeper (optional — not needed for today's win)</b></summary>

- **TCP/IP** is the family of rules underneath: IP addresses & routes packets; TCP guarantees they all arrive, in order (via a "handshake").
- Status codes you'll meet: **200** OK, **301/302** redirect, **404** not found, **500** server error.
- TLS sets up a shared secret key at the start so the rest of the conversation is encrypted — without ever sending the key in the clear.
- Big sites add **load balancers** to spread requests across many servers.
</details>

---
**New words** (also in `resources/glossary.md`): HTTPS, TLS, TLS certificate, CDN. (Plus the M5 basics: internet, IP address, DNS, client, server, request/response, HTTP, packet, router, port.)

**Source:** original — written for this course. Commands and the certificate inspection were verified by running them against a live site in the course's Linux (Codespaces) environment; the diagrams are original.
