# Lab 
M11: train your own AI and watch it learn

**You'll need:** a laptop with a **web browser** and ideally a **webcam**. **Nothing to install, no account.**
(No webcam? See the *Upload* note in Step 3.)
**Time:** ~30 minutes • **Work in your breakout pair** then try to fool each other's models.

> Heads up: this all runs *in your browser* your camera pictures stay on your own computer and
> nothing is uploaded. You can't break anything, and you can redo it as often as you like.

We'll teach a computer to tell two things apart say a **thumbs-up 👍** from a **thumbs-down 👎**
(pick any two things you can show your camera).

----------------------------------------------------------------------------------------

## Step 1: Open Teachable Machine
In your browser go to **teachablemachine.withgoogle.com** and click **Get Started**.

✅ **You should now see:** a choice of project types **Image**, **Audio**, and **Pose**.

## Step 2: Start an Image Project
Click **Image Project**, then **Standard image model**.

✅ **You should now see:** a workspace with empty **classes** (boxes labelled "Class 1", "Class 2"), a **Training** panel, and a **Preview** panel.

## Step 3: Name your two classes
Rename **Class 1** to your first thing (e.g. `Thumbs up`) and **Class 2** to your second (e.g. `Thumbs down`).

✅ **You should now see:** your two classes carry *your* names.
*(No webcam? Each class has an **Upload** button drag in ~20 photos per class instead.)*

## Step 4: Give the first class examples
On your first class, click **Webcam**, allow camera access, then **hold "Hold to Record"** while you show the pose for a few seconds.

✅ **You should now see:** a strip of **20–40 captured images** fill that class. More varied examples = a smarter model.

## Step 5: Give the second class examples
Do the same for the second class record a few seconds of the *other* thing.

✅ **You should now see:** both classes hold a batch of images. You've just built a **training set** the examples the model will learn from.

## Step 6: Train the model
Click **Train Model** and wait a few seconds (keep the tab in focus).

✅ **You should now see:** a progress indicator, then a "trained" state, and the **Preview** panel switches on. **That wait *was* the training** the model adjusting its weights to your examples.

## Step 7: Test it live (this is inference!)
Show your camera the first thing, then the second, and watch the **Preview** bars.

✅ **You should now see:** the prediction bars move in real time show a thumbs-up and the `Thumbs up` bar jumps toward 100%; switch and it flips. **Every guess is inference** the trained model deciding about something new, live.

## Step 8: Find its edges (and its bias)
Show it something you **didn't** train on, or test in different lighting/background from your examples.

✅ **You should now see:** the bars wobble or guess confidently *wrong*. The lesson: **a model only knows what you taught it** and if your examples were narrow or lopsided, so is the model. That's **bias**, live.

----------------------------------------------------------------------------------------------

## 🎉 Your win
You trained your own AI from examples and watched it **learn** (training) and **predict** live (inference) and saw firsthand how its examples (and their bias) shape what it can do.

**Post it to the chat wins board:** *"I trained an AI to tell ___ from ___ and fooled it with ___! 🎉"*

## Take-home (optional)
Retrain with **more and more varied** examples (different lighting, angles, distances) and watch the
predictions get steadier. That improvement *is* what "more and better data" buys in real AI.
