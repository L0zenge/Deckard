# Deckard 🔍📜🧙‍♂️
Created by L0zenge
Moo. 


<p align="center">
  <img src="image.png" alt="Deckard Cain" width="300px"/>
</p>

> *"Hello, my friend. Stay a while, and listen!"*

Sick of running into walls of text in the ToS, "contest rules", NDA, or Privacy statements that are worded to be as vague as possible, while fucking you as HARD as possible? They try leaving the door open for them to sell and sub-license your information, likeness, and ideas and train AI models off or your work to "remix" YOUR content into media that may will be "hereafter discovered in perpetuity". Or use wording like: The consent is perpetual and binding on the heirs and successors of the Entrants and Competitors.
They write terms in obfuscated, vague language and code so you don't know you're having your IP stolen. I response, we must use even nerdier language to scan their word-salad and inform the layman if they're getting taken advantage of or not. 
Protip: You are. This will just break down where and how hard. 

**Deckard** is a zero-dependency Horadric script that scans Terms of Service (TOS), contest rules, and NDAs for scamming AI bullshit and super-dense claude-clauses that are in there to steal your ACTUAL creativity. It unmasks modern corporate trap vernacular like AI training loops, data harvesting loopholes, hidden lawsuit bans, and arbitrary bot-disqualification triggers—before you accidentally sign away your creations to the Chaos Sanctuary.

---

## 🔮 What It Identifies

The script utilizes a custom Horadric Regex Pattern to flag 4 distinct schools of corporate malice:
* **The Future Theft Loophole:** Clauses like *"any and all media now known or hereafter discovered"* or *"reproductions in whole or in part"*, often used to stealthily feed your work, music, or art into generative AI training models.
* **Sublicensing & Perpetuity Traps:** Mechanisms used to sell or lease your property down the line while claiming their hands are clean.
* **Lawsuit Bans & Waivers:** Sneaky language designed to strip away your courtroom rights, force individual mandatory arbitration, or make you waive class-action rights.
* **Vague "Bot" Disqualifications:** Ambiguous text targeting "automated/3rd-party scripts" used to void contest payouts without providing any real physical proof of tampering.

---

## 📜 How to Use It

Because this tool is entirely self-contained within vanilla Python/Java/Notepad++ basic RegEx language, **you do not need to install any external dependencies or libraries**. It runs natively out of the box on Windows, macOS, and Linux. If I did it correctly, you shouldn't even need to run or extract/compile/launch anything. I've set this up so that it runs as if it's a webpage.
Side-effect: You don't have to be afraid of running malicious code.

If this stops running through the website however, you can use it the "correct" dev-nerd hyper1337h4x0r way:

### 1. Clone the Scroll
Clone this repository directly from your terminal:
```bash
git clone https://github.com
cd Deckard
```

### 2. Cast the Spell
Run the scanner by passing the target terms page URL as an argument.

🍏 **On macOS / Linux:**
```bash
python3 Deckard.py https://example-contest-rules.com
```

🪟 **On Windows:**
```cmd
python Deckard.py https://example-contest-rules.com
```
*(Note: On Windows, the script automatically triggers Virtual Terminal sequences to ensure the Horadric UI text colors and the legendary identity chime run flawlessly in Command Prompt and PowerShell).*

---

## ⚡ The Identification Sequence

When you run a scroll through the scanner, you will witness the classic Horadric Identification ritual:
1. **The Greeting:** Cain acknowledges your arrival.
2. **The Ritual:** The script fetches the document, pops the scroll casing, and runs the identification sequence (`*click* ...tick... ➔ WHOOOOOSH! ✨`).
3. **The Reveal:** Any problematic text blocks are illuminated in bold red highlighting alongside unique diagnostic insight from Cain himself.

---

## ⚖️ License
This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
