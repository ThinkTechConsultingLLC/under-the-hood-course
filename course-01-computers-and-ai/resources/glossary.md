# Glossary — Course 01

*Plain-language definitions, in the words a first-day beginner would understand.*
*Every new term introduced in a module gets a line here. Kept alphabetical.*

**Argument** — the *what* you give a command to act on, usually a file or folder name (in `ls Documents`, the argument is `Documents`). *(M3)*

**Artificial intelligence (AI)** — the broad umbrella term for any computer doing something that seems "smart." *(M11)*

**Authentication** — proving you are who you say you are (with a password, a code, or a key). *(M6)*

**Avalanche effect** — changing even one character of the input produces a completely different hash; why a tiny edit scrambles the whole fingerprint. *(M6)*

**Bias (in AI)** — unfairness a model picks up from lopsided training data, making it work worse for some inputs or groups. *(M11)*

**Binary** — the 0s-and-1s code a computer thinks in; every 0 or 1 is like a switch that's off or on. *(M1)*

**BIOS** — older PC firmware that starts the computer before the OS loads; **UEFI** is its modern replacement. *(M2)*

**Bit** — the smallest piece of information a computer holds: a single 0 or 1. *(M1)*

**Booting** — the start-up sequence from power-on to a usable desktop: power → firmware → bootloader → OS. *(M2)*

**Bootloader** — a small program the firmware runs whose job is to load the operating system. *(M2)*

**Branch** — a separate line of work in a repo where you can try changes without touching the main version, then merge them in. *(M7)*

**Byte** — a small group of 8 bits, about one letter's worth of information. Sizes like GB and TB are just huge piles of bytes. *(M1)*

**CDN (content delivery network)** — copies of a website cached on servers worldwide, so it loads fast from a nearby one. *(M5)*

**Client** — the device that asks for something on a network — like your laptop or phone opening a website. *(M5)*

**Client/server** — the everyday pattern of the web: a client asks (a request) and a server answers (a response). *(M5)*

**Clock speed (GHz)** — how many basic steps a CPU takes per second; 2.4 GHz ≈ 2.4 billion per second. Higher = faster at each step. *(M1)*

**Clone** — make a local copy of a remote repository (e.g. download one from GitHub). *(M7)*

**Cloud computing** — renting computers and services over the internet (in data centers) instead of owning them. *(M8)*

**Command** — a word you type to make the computer do something (like `ls` to list files). *(M3)*

**Command line** — the way of controlling a computer by typing commands instead of clicking; the text-based interface to the shell. *(M3)*

**Commit** — a saved snapshot of your project at a point in time, with a message describing what changed. *(M7)*

**Container** — a sealed box holding an app plus everything it needs to run, fenced off from the rest of the computer so it runs the same anywhere. *(M10)*

**Context window** — how much text (in tokens) an LLM can hold in view at once; anything beyond it drops out of sight. *(M12)*

**Control group (cgroup)** — a Linux feature that limits how much CPU/memory a process may use; one half of how containers work. *(M4)*

**CPU (processor / chip)** — the part that does the work: every calculation and task runs through it. *(M1)*

**CPU core** — one independent worker inside a CPU; more cores means more things genuinely done at once. *(M1)*

**Current working directory** — the folder you are currently "standing in" at the command line; `pwd` prints it. *(M3)*

**Daemon** — a program that runs quietly in the background with no window, providing a service. *(M4)*

**Data center** — a warehouse full of thousands of computers working together; what "the cloud" is physically made of. *(M1)*

**Deep learning (DL)** — machine learning done with many-layered neural networks; it powers most of today's AI breakthroughs. *(M11)*

**DNS (Domain Name System)** — the internet's phone book: it turns a website's name (like `example.com`) into its number, the IP address. *(M5)*

**Docker** — the most popular tool for building, sharing, and running containers. *(M10)*

**Docker Hub** — the big public registry where container images are stored and shared online. *(M10)*

**Dockerfile** — a short plain-text recipe that lists what to put inside an image; you build it into the image. *(M10)*

**Driver** — a small program that lets the OS talk to a specific piece of hardware (printer, GPU, Wi-Fi, etc.). *(M2)*

**Encryption** — scrambling data so only someone with the key can read it; reversible (unlike a hash). *(M6)*

**File** — a named container of data: a document, photo, song, or app. *(M2)*

**File extension** — the bit after the dot in a filename (like `.pdf` or `.jpg`) that hints at what kind of file it is. *(M2)*

**File manager** — the app for browsing your files and folders (Finder on Mac, File Explorer on Windows, Files on Linux/Chromebook). *(M2)*

**Filesystem** — the whole tree of folders and files on your computer. *(M2)*

**Firmware** — tiny permanent software baked into a chip that runs first at power-on to start the machine. *(M2)*

**Folder (directory)** — a container that holds files and other folders; "directory" is the same thing by another name. *(M2)*

**GB (gigabyte)** — a unit for how much a computer can hold; about a billion bytes. Used for both RAM and storage sizes. *(M1)*

**Git** — the standard version-control tool: it tracks every change to your files so you can review, compare, or undo them. Runs on your own computer. *(M7)*

**GitHub** — a cloud service that hosts Git repositories — for backup, sharing, and collaboration (GitLab and Bitbucket are alternatives). *(M7)*

**GPU (graphics processing unit)** — a chip with thousands of small cores, great at doing the same calculation across lots of data at once; used for graphics and for AI. *(M1)*

**Guest OS** — the operating system running inside a virtual machine (as opposed to the host's). *(M9)*

**Hallucination** — when an LLM confidently produces plausible-sounding text that is actually wrong or invented (it predicts likely text, it doesn't check facts). *(M12)*

**Hardware** — the physical parts of a computer you could actually touch (screen, keyboard, the chips inside). *(M1)*

**Hash** — a one-way scrambled fingerprint of data: same input → same hash, can't be reversed; how passwords are safely stored. *(M6)*

**HDD (hard disk drive)** — older storage using spinning magnetic platters; cheap and roomy, but slow and mechanical. *(M1)*

**Home folder (home directory)** — your personal area where Documents, Downloads, and Pictures live; your starting point in the file manager (and where the terminal starts — `cd` on its own returns there). *(M2)*

**Host OS** — the operating system of the real machine that runs virtual machines or containers. *(M9)*

**HTML** — the code that describes a web page's content and structure; your browser reads it and draws the page you see. *(M5)*

**HTTP** — the language browsers and web servers use to ask for and send web pages; a reply code of `200` means "success, here's the page." *(M5)*

**HTTPS** — HTTP wrapped in TLS encryption; the padlock means your connection to the site is scrambled and private. *(M5)*

**Hypervisor** — the software that creates and runs virtual machines, sharing one real computer's hardware among them. *(M9)*

**IaaS (Infrastructure as a Service)** — renting a bare machine in the cloud; you install and manage everything on it. *(M8)*

**Image (container image)** — the read-only template a container is made from: the app and all its ingredients packaged together. Like a recipe. *(M10)*

**Inference** — the "using" phase of a model: it takes something new and makes a prediction (fast, every time you use it). *(M11)*

**Input** — anything you give the computer (a keypress, a click, a tap). *(M1)*

**Input device** — a part you use to give the computer something: keyboard, mouse, microphone, camera. *(M1)*

**Internet** — a network of networks: millions of smaller networks joined together so any connected device can reach any other. *(M5)*

**IP address** — a device's unique address on a network (like `74.125.19.147`), so messages know where to go and where to come back. *(M5)*

**Isolation** — keeping a program fenced off so it can't clash with other programs or interfere with the rest of the computer. *(M10)*

**KB (kilobyte)** — a small size unit; roughly a paragraph of text. About 1,000 bytes. *(M1)*

**Kernel** — the core of an operating system: it loads at boot and manages programs, memory, and hardware. (It's also the part containers share with the host — M6.) *(M2)*

**Kubernetes** — the dominant tool for running and managing many containers across many servers (a container "orchestrator"). *(M10)*

**Labelled data** — examples that come with the right answer attached (e.g. photos each tagged "cat" or "not cat"); what a model learns from. *(M11)*

**LAN (Local Area Network)** — a small network covering one place, like a home or an office. *(M5)*

**Large language model (LLM)** — a deep-learning model trained on huge amounts of text to predict words; the engine behind chatbots. *(M11)*

**Machine learning (ML)** — the kind of AI where a computer learns patterns from examples instead of following hand-written rules. *(M11)*

**Latency** — the delay before a response; lower is better, and a data center closer to you helps. *(M8)*

**Least privilege** — giving each user or program only the access it needs, so a breach can't reach everything. *(M6)*

**MB (megabyte)** — a medium size unit; roughly a photo. About 1,000 KB. *(M1)*

**Merge** — combine the changes from one branch into another. *(M7)*

**Model** — what machine learning produces: the trained thing that takes an input and makes a prediction. *(M11)*

**Motherboard** — the big board inside the computer that everything else plugs into and connects through. *(M1)*

**Multitasking** — the OS creating the illusion of doing many things at once by switching the CPU between programs very fast. *(M4)*

**Namespace** — a Linux feature that limits what a process can *see* (its own files, process list, network); the other half of how containers work. *(M4)*

**Network** — two or more computers linked together so they can share files, devices, or a connection. *(M5)*

**Neural network** — a web of simple connected units whose connection strengths ("weights") are tuned during training; the core of deep learning. *(M11)*

**Next-token prediction** — the one trick an LLM does: repeatedly guess the most likely next chunk of text and add it. *(M12)*

**Operating system (OS)** — the master program that runs your computer: it launches programs, shares the CPU and memory, talks to the hardware, and keeps your files and users organized (Windows, macOS, Linux, ChromeOS). *(M2)*

**Option (flag)** — the *how* of a command, usually a dash and a letter (in `ls -l`, the option `-l` asks for a long, detailed list). *(M3)*

**Orchestration** — automatically running, scaling, and healing many containers across servers; Kubernetes is the main tool. *(M10)*

**Output** — anything the computer gives back (text on screen, a sound, a printout). *(M1)*

**Output device** — a part the computer uses to give you something back: screen, speakers, printer. *(M1)*

**Owner / group / world** — the three audiences a file's permissions apply to: its owner (you), a group of users, and everybody else. *(M4)*

**PaaS (Platform as a Service)** — the cloud runs the machine and OS; you just bring your code (e.g. Codespaces). *(M8)*

**Packet** — a small chunk of a larger message; data is split into packets that travel separately and are reassembled at the other end. *(M5)*

**Parallelism** — doing many calculations at the same time instead of one after another; what GPUs are built for (and why AI uses them). *(M1)*

**Password manager** — an app that generates and remembers a unique, strong password for every site. *(M6)*

**Patching** — installing updates that fix known security bugs; closing doors attackers walk through. *(M6)*

**Path** — the route to a file or folder through the tree of folders (like `Documents/work/notes.txt`). *(M2)*

**Permissions** — the rules on a file saying who may read it, change it, or run it; they protect users (and you) from accidents and each other. *(M4)*

**Phishing** — a scam message that tricks you into giving up a password or clicking malware. *(M6)*

**PID (process ID)** — the number the OS gives each running process so it can be pointed at (e.g. to stop it). *(M4)*

**Pipe (`|`)** — sends one command's output straight into another command as its input, so small commands snap together (e.g. `ls | wc -l`). *(M3)*

**Port** — a numbered "door" on a computer that a program listens at; e.g. web servers usually use port 80. *(M10)*

**Portability** — the quality of running the same way on any computer; a container's big selling point ("build it once, run it anywhere"). *(M10)*

**Process** — the work the computer does between input and output, handled by the CPU. *(M1)*

**Process (running program)** — a program that is currently running, with its own PID and slice of memory; what you see listed in the process viewer. *(M4)*

**Process viewer** — the app that lists everything running and how much CPU/memory each uses: Activity Monitor (Mac), Task Manager (Windows), System Monitor (Linux/Chromebook). *(M4)*

**Prompt** — the bit of text (often ending in `$`) that means the shell is ready for you to type a command. *(M3)*

**Prompt (to an LLM)** — the text you give a chatbot; because the model continues your text, a clearer prompt gets a better answer. *(M12)*

**Protocol** — an agreed-on set of rules for how devices talk, so both sides understand each other. *(M5)*

**Pull** — fetch commits from a remote (e.g. GitHub) and apply them to your local repo. *(M7)*

**Push** — send your local commits up to a remote (e.g. GitHub). *(M7)*

**RAM (memory)** — the computer's short-term memory for whatever you're doing right now; it's wiped clean when the power goes off. *(M1)*

**Redirection (`>` `>>`)** — sends a command's output into a file instead of the screen; `>` replaces the file, `>>` adds to the end. *(M3)*

**Region** — a geographic location where a cloud provider runs data centers; pick one near your users to cut latency. *(M8)*

**Registry** — an online store for container images that you can pull from and push to; Docker Hub is the best-known one. *(M10)*

**Remote** — a copy of a repository hosted elsewhere (usually on GitHub) that you push to and pull from. *(M7)*

**Repository (repo)** — a project folder that Git is tracking, including its full history of commits. *(M7)*

**Router** — a device that connects networks and forwards packets one hop closer to their destination. *(M5)*

**SaaS (Software as a Service)** — finished software you just use in a browser; you manage nothing (Gmail, Netflix). *(M8)*

**Scalability** — the ability to add or remove computing power on demand as load rises and falls. *(M8)*

**Scheduler** — the part of the OS that rapidly switches the CPU between processes so many can run "at once". *(M4)*

**Secure Boot** — a UEFI feature that checks the OS hasn't been tampered with before it's allowed to load. *(M2)*

**Server** — a computer whose job is to serve things up; it answers clients' requests (for example, sends back a web page). *(M5)*

**Shell** — the program that reads the commands you type and tells the operating system to carry them out. *(M3)*

**Software** — the instructions running on the hardware: the apps, games, and pages you use. *(M1)*

**Specs (specifications)** — the list of what's inside a particular computer (its CPU, RAM, storage, and so on). *(M1)*

**SSD (solid-state drive)** — modern storage using flash chips with no moving parts; much faster and tougher than an HDD, and now standard. *(M1)*

**Storage** — the computer's long-term memory that keeps your files, photos, and apps even when the power is off. *(M1)*

**Swap (virtual memory)** — storage the OS uses as overflow when RAM fills up; it keeps things running but is much slower than RAM. *(M4)*

**Tab completion** — pressing the Tab key to let the shell finish a half-typed file or folder name for you. *(M3)*

**Superuser (root / admin)** — the special user account that can override any permission; why installing software asks for your password. *(M4)*

**TB (terabyte)** — a larger storage unit; about 1,000 GB. *(M1)*

**TCP/IP** — the main family of rules that makes the Internet work: IP gets packets to the right address, TCP makes sure nothing is lost and everything arrives in order. *(M5)*

**Terminal** — the window you type commands into; it gives you access to the shell. *(M3)*

**Thread** — a task a CPU core works on; a trick lets one core juggle two threads, so an 8-core chip may show "16 threads". *(M1)*

**Threat model** — a quick plan of what's valuable, who might want it, and how they'd try to get it. *(M6)*

**TLS** — the encryption that secures web connections (the "S" in HTTPS); older versions were called SSL. *(M5)*

**TLS certificate** — a verifiable ID card a trusted authority issues a website, so your browser knows it's genuine, not an impostor. *(M5)*

**Token** — a small chunk of text (a short word, a word-piece, or a space) — the unit an LLM reads and predicts. *(M12)*

**Training** — the "learning" phase of a model: it sees many examples and adjusts itself to get better (slow, done occasionally). *(M11)*

**Training cutoff** — the date a model's training data stops; it has no built-in knowledge of anything after it. *(M12)*

**Training set** — the collection of labelled examples a model learns from during training. *(M11)*

**Transformer** — the neural-network design (2017) behind modern AI; it handles context well and keeps improving as you add data and compute. *(M11)*

**Transistor** — a microscopic on/off switch; a CPU is built from billions of them — how 0s and 1s become physical. *(M1)*

**Two-factor authentication (2FA)** — a second proof beyond your password (a phone code, app, or key), so a stolen password isn't enough. *(M6)*

**UEFI** — modern PC firmware (replaces BIOS): starts the computer, handles big disks, and adds Secure Boot. *(M2)*

**Version control** — a system that saves snapshots of your work over time so you can see history, undo, and collaborate without overwriting each other. *(M7)*

**Virtual machine (VM)** — a whole computer, with its own full guest OS, created by a hypervisor inside a real one; heavier and slower than a container. *(M9)*

**Virtualization** — software that makes one real computer act like many separate ("virtual") computers. *(M9)*

**WAN (Wide Area Network)** — a network that spans a large area, such as a city, country, or the world. *(M5)*

**Weights** — the adjustable connection strengths inside a neural network; "learning" is the tuning of these numbers. *(M11)*
