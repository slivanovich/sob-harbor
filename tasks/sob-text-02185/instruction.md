Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Duplicate Boy: Duplicate Boy (Ord Quelu of the planet Lallor) is a fictional superhero in the DC Comics Universe first appearing in a story by science fiction writer Edmond Hamilton in "Adventure Comics" #324 (September 1964).  Hamilton had created a backstory for Duplicate Boy, who was first submitted as a super hero concept to DC comics by a young fan, Thea Temple, in 1963, who received acknowledgment from the company.  Duplicate Boy appeared as a supporting character in the Legion of Super-Heroes titles, set approximately a thousand years in the future, and is one of the most powerful beings in that time-frame.

Legion of Super-Heroes: The Legion of Super-Heroes is a fictional superhero team appearing in American comic books published by DC Comics.  Created by writer Otto Binder and artist Al Plastino, the Legion is a group of superpowered beings living in the 30th and 31st centuries of the DC Comics Universe , and first appears in "Adventure Comics" #247 (April 1958).

Jessica Cruz: Jessica Cruz is a fictional comic book superhero appearing in books published by DC Comics.  Created by Geoff Johns and Ethan Van Sciver, she is a member of the Green Lantern Corps and the Justice League.  Her first full appearance takes place in "Justice League" #31 (August 2014), which is also her first cover appearance.

Doll Man: Doll Man is a fictional superhero from the Golden Age of Comics, originally published by Quality Comics and currently part of the DC Comics universe of characters.  Doll Man was created by cartoonist Will Eisner and first appeared in a four-page story entitled "Meet the Doll Man" in "Feature Comics" #27.  The issue's December, 1939 cover date indicates that Doll Man is the first comic book superhero with a shrinking power.  He notably predates the more-famous Ray Palmer and Hank Pym by two decades.

Captain Cold: Captain Cold (Leonard Snart) is a fictional supervillain appearing in American comic books published by DC Comics.  Captain Cold is the leader of the Rogues, a loose criminal association, as well as the older brother of Golden Glider.  He also has served as a bitter enemy to the Silver Age Flash Barry Allen, both enemy and grudging friend to the third Flash Wally West, and one of the killers of the fourth Flash Bart Allen.

Invisible Hood: The Invisible Hood is a fictional superhero in the DC Comics Universe.  He was originally owned by Quality Comics, but was later acquired by DC Comics, along with other Quality characters.  He first appeared in "Smash Comics" #1 (August 1939), and was created by Art Pinajian, Pinajian illustrated the story under the pseudonym "Art Gordon".

Bart Allen: Bart Allen is a fictional superhero in the DC Comics Universe .  Allen first appeared as the superhero Impulse, a teenage sidekick of the superhero the Flash, before later on becoming the second hero known as Kid Flash.  The character first made a cameo appearance in "The Flash" #91 in 1994, while his first full appearance in issue #92, and appeared as the lead character in "Impulse" (1995–2002) and "The Flash: The Fastest Man Alive" (2006–2007).  In the latter series, the character became the fourth hero to assume the identity of The Flash.  Bart also prominently features in the superhero team titles "Young Justice" and "Teen Titans".  As the Flash, Bart was also a core character in 10 issues of "Justice League of America".

Mister America (Jeffrey Graves): Mister America (Jeffrey Graves) is a fictional superhero in the DC Comics Universe, the official third and current character to take up the Mr. America mantle and a member of the superhero team the Justice Society of America.  Mr. America made his first full appearance as Jeffrey Graves in "Justice Society of America" (vol.  3) #4 (May 2007) and was created by Geoff Johns and Dale Eaglesham.

Champions of Angor: The Champions of Angor (also known as the Justifiers, the Assemblers and the Meta Militia) are a fictional superhero team in the DC Comics universe.  They are a pastiche of the Avengers from the Marvel Comics universe.  They were created by Mike Friedrich and Dick Dillin in the pages of Justice League of America #87 February (1971).

Gay Ghost: The Gay Ghost (later renamed the Grim Ghost, not to be confused with Grim Ghost) is a fictional superhero in the DC Comics universe whose first appearance was in "Sensation Comics" #1 (Jan. 1942), published by one DC's predecessor companies, All-American Publications.  He was created by writer Gardner Fox and artist Howard Purcell.

Question: In which issue did this fictional superhero in the DC Comics Universe, who was killed by Captain Cold, make his first full appearance?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "superhero_identified": {
      "type": "object",
      "description": "Details of the superhero identified from the context based on the description.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The primary name of the superhero."
        },
        "aliases": {
          "type": "array",
          "description": "Other superhero identities or aliases used by the character.",
          "items": {
            "type": "string"
          }
        },
        "flash_incarnation_number": {
          "type": "integer",
          "description": "The sequential number of this character as an incarnation of The Flash."
        }
      },
      "required": [
        "name",
        "aliases",
        "flash_incarnation_number"
      ],
      "additionalProperties": false
    },
    "villain_identified": {
      "type": "object",
      "description": "Details of the villain mentioned in the context as having killed the superhero.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the villain."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "event_details": {
      "type": "object",
      "description": "Details about the significant event linking the superhero and villain.",
      "properties": {
        "killed_by_villain": {
          "type": "boolean",
          "description": "Indicates whether the superhero was killed by the identified villain."
        }
      },
      "required": [
        "killed_by_villain"
      ],
      "additionalProperties": false
    },
    "first_full_appearance_details": {
      "type": "object",
      "description": "Details regarding the superhero's first full appearance in a comic.",
      "properties": {
        "comic_series": {
          "type": "string",
          "description": "The title of the comic series where the first full appearance occurred."
        },
        "issue_number": {
          "type": "string",
          "description": "The specific issue number of the first full appearance."
        },
        "year": {
          "type": "integer",
          "description": "The year of the first full appearance."
        }
      },
      "required": [
        "comic_series",
        "issue_number",
        "year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "superhero_identified",
    "villain_identified",
    "event_details",
    "first_full_appearance_details"
  ],
  "additionalProperties": false
}
