import re
import argparse
import sys
import random
import time
import os
import urllib.request
from urllib.error import URLError, HTTPError

# Force Windows command prompt to recognize ANSI color text & formatting
if os.name == 'nt':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# Universal text color definitions
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# The Horadric Regex Pattern 
SCAM_PATTERN = re.compile(
    r"\b(?P<sublicense>sub[- ]?licens(?:e|ing))|"
    r"\b(?P<perpetuity>in perpetuity|perpetual)\b|"
    r"\b(?P<media_trap>any (?:and )?all media|hereafter discovered)\b|"
    r"\b(?P<derivative>deriv(?:a|i)tive work)\b|"
    r"\b(?P<whole_part>reproduction[s]? (?:either )?in whole or in part)\b|"
    r"\b(?P<lawsuit_ban>waive[r]? (?:moral|class|jury)|class[- ]action|dispute[s]? resolved (?:exclusively )?by|agree not to sue|waive.*right to.*(?:sue|court|litigate))\b|"
    r"\b(?P<bot_trap>(?:bot|robot(?:ic)?|automat(?:ed|ion)|script|third[- ]party|3rd[- ]party).+?(?:tamper|cheat|disqual|manipulat))\b|"
    r"\b(?P<ai_train>(?:generat(?:e|ive)|train|feed|model|algorithm|synthesiz).+?(?:material|submit|work|content|data))\b",
    re.IGNORECASE | re.DOTALL
)

# Horadric Translation Matrix (Layman's Terms Map)
LAYMAN_TRANSLATIONS = {
    "sublicense": "They want the right to legally rent, lease, or outright sell your data/creations to third-party tech giants to train outside AI models—and your hands will be legally tied.",
    "perpetuity": "This contract outlives you. 'Forever' means even if you delete your account, quit the industry, or pass away, they (and anyone they sell your work to) retain the legal right to use it.",
    "media_trap": "The ultimate AI training model loophole. By pre-consenting to future media forms 'hereafter discovered,' you are giving them prior permission to feed your audio/visuals into algorithm engines.",
    "derivative": "They want to generate 'similar but different' content based strictly on your style, melodies, or timbres without having to pay you a single cent for the new variation.",
    "whole_part": "They can chop your track into pieces, isolate your vocals, or steal specific melodies. In AI music generation, this lets them isolate your 'stems' to train machine components.",
    "lawsuit_ban": "You cannot sue them in an actual courtroom, and you cannot join forces with other scammed creators. Any fight must be fought completely alone in front of a private, closed-door corporate arbitrator.",
    "bot_trap": "They can kick you out of the competition whenever they want without providing a shred of hard technical proof. They can blame 'suspicious scripts' to void a massive payout completely unchecked.",
    "ai_train": "They are explicitly telling you they intend to harvest your submission to train internal models, build automated promotional tools, or synthetically replicate your work layout."
}

CAIN_WARNINGS = [
    "This text contains a great evil, the likes of which I have not seen since the fall of Tristram!",
    "Ah, the signature of the Dark Wanderer is all over this clause...",
    "By the three! This passage attempts to consume your very soul and your creations!",
    "It is as I feared... They seek to bind your works to the Burning Hells in perpetuity.",
    "A clever deception! Diablo himself could not have crafted a more devious trap.",
    "Look here, my friend! This phrasing is a manifestation of pure corporate malice."
]

def play_identify_sound():
    sys.stdout.write(f"\n{Colors.WARNING}[*click*]{Colors.ENDC} Uncapping the scroll case... ")
    sys.stdout.flush()
    time.sleep(0.4)
    
    sys.stdout.write(f"{Colors.BOLD}...tick...{Colors.ENDC} ")
    sys.stdout.flush()
    sys.stdout.write("\a")
    sys.stdout.flush()
    time.sleep(0.5)
    
    whoosh_frames = [
        f"{Colors.BLUE}➔ w{Colors.ENDC}",
        f"{Colors.BLUE}➔ wh{Colors.ENDC}",
        f"{Colors.BLUE}➔ whoo{Colors.ENDC}",
        f"{Colors.BLUE}➔ whoooo{Colors.ENDC}",
        f"{Colors.BLUE}{Colors.BOLD}➔ WHOOOOOSH! ✨{Colors.ENDC}"
    ]
    
    for frame in whoosh_frames:
        sys.stdout.write(f"\r{Colors.BLUE}Unrolling scroll at:{Colors.ENDC} {frame}")
        sys.stdout.flush()
        time.sleep(0.12)
    print("\n")

def clean_html(html_content):
    text = re.sub(r'<script[\s\S]*?>[\s\S]*?<\/script>', '', html_content)
    text = re.sub(r'<style[\s\S]*?>[\s\S]*?<\/style>', '', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def fetch_url_text(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
        return clean_html(html)
    except HTTPError as e:
        print(f"\n{Colors.FAIL}[Cain]{Colors.ENDC} The gateway is barred, my friend! The server rejected us. HTTP Status: {e.code}")
        sys.exit(1)
    except URLError as e:
        print(f"\n{Colors.FAIL}[Cain]{Colors.ENDC} I cannot reach this location. The pathways are blocked. Reason: {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.FAIL}[Cain]{Colors.ENDC} An unknown shadow has interrupted our reading: {e}")
        sys.exit(1)

def scan_text(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    matches_found = 0

    print(f"{Colors.HEADER}{Colors.BOLD}=== THE HORADRIC SCROLL OF IDENTIFICATION ==={Colors.ENDC}\n")

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
            
        match = SCAM_PATTERN.search(sentence)
        if match:
            matches_found += 1
            
            # Identify which specific capturing group was triggered
            triggered_group = None
            matched_text = match.group(0)
            for group_name, value in match.groupdict().items():
                if value is not None:
                    triggered_group = group_name
                    matched_text = value
                    break
            
            # Highlight the culprit phrase inside the text snippet
            highlighted_sentence = sentence.replace(
                matched_text, f"{Colors.FAIL}{Colors.BOLD}{matched_text}{Colors.ENDC}"
            )
            
            # Retrieve the appropriate layman translation or use a generic fallback
            layman_translation = LAYMAN_TRANSLATIONS.get(
                triggered_group, "They are trying to sneak obscure legal jargon past your eyes."
            )
            
            cain_quote = random.choice(CAIN_WARNINGS)
            print(f"{Colors.WARNING}[DESTRUCTION BLOCK #{matches_found}]{Colors.ENDC} \"{cain_quote}\"")
            print(f"  {Colors.BOLD}📜 Raw Line:{Colors.ENDC} ... {highlighted_sentence} ...")
            print(f"  {Colors.GREEN}💡 Layman's Terms:{Colors.ENDC} {layman_translation}\n")
            time.sleep(0.15) 

    if matches_found == 0:
        print(f"{Colors.GREEN}✓ \"You have quite a treasure there in that document! It appears clean of immediate corruption.\"{Colors.ENDC}\n")
    else:
        print(f"{Colors.FAIL}✖ \"Our worst fears are realized. I have identified {matches_found} corruptions. Do not sign this, lest your soul belong to them!\"{Colors.ENDC}\n")

def main():
    parser = argparse.ArgumentParser(description="Let Deckard Cain identify the ancient evils inside a terms page.")
    parser.add_argument("url", help="The scroll (URL) containing the text to identify.")
    args = parser.parse_args()

    print(f"\n{Colors.BLUE}\"Hello, my friend. Stay a while, and listen!\"{Colors.ENDC}")
    print(f"\"You want me to identify the items within this text? Let me see...\"")
    
    document_text = fetch_url_text(args.url)
    play_identify_sound()
    scan_text(document_text)

if __name__ == "__main__":
    main()
