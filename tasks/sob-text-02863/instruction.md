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
Mixed Martial Arts Pakistan: Mixed Martial Arts Pakistan (or PAK MMA) is the premiere mixed martial arts (MMA) and martial arts promotion based in Pakistan that was created in December 2007 by Bashir Ahmad to promote martial arts (and martial sports such as boxing and wrestling) styles in Pakistan with a particular focus on mixed martial arts competition.

Yushin Okami: Yushin Okami (岡見 勇信 , Okami Yūshin , born July 21, 1981) is a Japanese mixed martial artist currently competing in the Light Heavyweight division of the UFC.  A professional competitor since 2002, Okami has also formerly competed for PRIDE, Pancrase, M-1 Global, World Series of Fighting, and Professional Fighters League.  He holds notable wins over Mark Munoz, Hector Lombard, Alan Belcher (twice),Anderson Silva (Via DQ), Nate Marquardt, former MMA fighter Evan Tanner and Mike Swick.

Bertrand Amoussou-Guenou: Bertrand Amoussou-Guenou (born May 29, 1966) is a retired French mixed martial artist and judoka.  He is a trainer for his younger brother Karl of "Team Amoussou" and, following official recognition of mixed martial arts in France, became the president of the national sanctioning body, the Commission National de Mixed Martial Arts, in January 2008.  On 1 October 2013, Amoussou assumed the position of president of the International Mixed Martial Arts Federation (IMMAF).

Cage Force: Cage Force(former name Demolition Octagon Gear (D.O.G.)) is a defunct Japanese Mixed Martial Arts (MMA) organization operated by Greatest Common Multiple (GCM) Communication.  It was the first Japanese MMA organization to feature an octagon cage instead of a ring.  Yushin Okami, Eiji Mitsuoka, Kuniyoshi Hironaka and Keita Nakamura experienced a cage match in D.O.G before contract with UFC.  It enforced the Unified Rules of Mixed Martial Arts when the changed name to "Cage Force" from "D.O.G.", to prepare Japanese MMA fighters for the UFC.  Cage Force tournament winner was entitled to a contract with UFC.  Yoshiyuki Yoshida and Takeya Mizugaki have been contracted to the UFC and WEC by winning the tournament.

Hikaru Sato: Hiroaki Sato (佐藤 弘明 , Satō Hiroaki , born July 8, 1980) is a Japanese professional wrestler and mixed martial artist, better known by the ring name Hikaru Sato (佐藤 光留 , Satō Hikaru ) .  Sato started his MMA career in February 2000, fighting for Pancrase Hybrid Wrestling.  During the next eight years, Sato fought, on average, five times a year, compiling a record of 18 wins, 19 losses and four draws, which included fights against the likes of Keiichiro Yamamiya, Nathan Marquardt, Ryo Chonan and Yushin Okami.  In May 2008, Sato transitioned into the world of professional wrestling, when he was signed by the Dramatic Dream Team (DDT) promotion.  He has since had ten MMA fights.  In November 2010, Sato first became a triple crown trios champion with Michael Nakazawa and Tomomitsu Matsunaga and then also won DDT's top singles title, the KO-D Openweight Championship.  Sato remained affiliated with DDT until January 2014.  He is currently working for the All Japan Pro Wrestling promotion, where he is a former two-time World Junior Heavyweight Champion and three-time All Asia Tag Team Champion, while also being a three-time winner of the Jr.  Tag Battle of Glory tournament.

Nate Marquardt: Nathan Joel "Nate" Marquardt (born April 20, 1979) is an American mixed martial artist competing in the middleweight division of the Ultimate Fighting Championship.  A professional competitor since 1999, he is a former Strikeforce Welterweight Champion and a three-time Pancrase Middleweight Champion.

Mohammed &quot;The Hawk&quot; Shahid: Mohammed Shahid (born July 8, 1989) is an entrepreneur and a mixed martial artist from Bahrain.  He is the CEO of KHK MMA and the President of the Bahrain based mixed martial arts organisation, Brave Combat Federation owned and supported by His Highness Sheikh Khalid bin Hamad Al Khalifa.  Mohammed Shahid was the first mixed martial artist from Bahrain to compete in global MMA events.  He was assigned a managerial role to develop mixed martial arts in Bahrain as the CEO of KHK MMA.  Bahrain established a national team alongside bringing global talent to facilitate the growth of MMA in Bahrain.

Genki Sudo: Genki Sudo (須藤 元気 , Sudō Genki , born March 8, 1978 in Kōtō, Tokyo, Japan) is a Japanese singer, composer, choreographer, actor, professional calligrapher and author.  He is the producer, director, and former lead vocalist of the music group World Order, which is known for their techno music style and highly synchronised robotic choreography.  Sudo is a retired mixed martial artist and a kickboxer who, until December 31, 2006 competed in the Japanese fighting organization HERO'S and before that, the Ultimate Fighting Championship and Pancrase.  He is known for his elaborate ring entrances and unorthodox fighting style.  Over his career he holds notable wins over Nate Marquardt, Eric "Butterbean" Esch, Mike Brown, Kazuyuki Miyata, Hiroyuki Takaya, Damacio Page and Ramon Dekkers.

UFC 122: UFC 122: Marquardt vs. Okami was a mixed martial arts event held by the Ultimate Fighting Championship on November 13, 2010 at König Pilsener Arena in Oberhausen, Germany.  This event aired on the same day, via tape delay, on Spike TV in the U.S.

UFC 126: Former Light Heavyweight Champion Vitor Belfort was scheduled to fight Yushin Okami at UFC 122.  However, UFC President Dana White said that Belfort would instead challenge Middleweight Champion Anderson Silva for the belt.  Belfort was originally scheduled to compete against Silva on January 2, 2010 at UFC 108, but due to an injury sustained by Silva, the fight had to be postponed until February 6, 2010 at UFC 109 and April 10, 2010 at UFC 112, respectively.  However, both fights were cancelled.

Question: Who is the older mixed martial artiest, Yushin Okami or Nate Marquardt?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "older_fighter": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "younger_fighter": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "comparison_summary": {
      "type": "string",
      "description": "Summary of who is older based on birth dates."
    },
    "is_older_fighter_correct": {
      "type": "boolean",
      "description": "True if the identified older fighter is indeed older."
    }
  },
  "required": [
    "older_fighter",
    "younger_fighter",
    "comparison_summary",
    "is_older_fighter_correct"
  ],
  "additionalProperties": false
}
