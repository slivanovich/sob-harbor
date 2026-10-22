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
Henri van Opstal: Henri van Opstal (born February 20, 1989) is a Dutch kickboxer who competes in the middleweight division.  Van Opstal came to prominence by winning the WMC European Junior Middleweight Championship but found further success competing in Japan, taking wins over a number of the countries' top middleweights and finishing as runner-up in the "Shoot Boxing World Tournament 2012".

Jerrel Venetiaan: Jerrel Venetiaan (born March 9, 1971) is a retired Dutch kickboxer and mixed martial artist who has fought in Pride Fighting Championships, K-1 and RINGS Holland.  In MMA, he holds notable wins against Daijiro Matsui and RINGS veteran Joop Kasteel.  In kickboxing, he was the champion of two K-1 GPs and defeated talented kickboxers such as Remy Bonjasky, Bjorn Bregy, Xhavit Bajrami and Jorgen Kruth.

Ricardo Arona: Ricardo Arona (] ; born July 17, 1978) is a retired Brazilian mixed martial artist.  He has competed in PRIDE Fighting Championships and RINGS in his mixed martial arts career, and was a member of Brazilian Top Team.  He is the former RINGS Middleweight Champion, as well as the 2001 RINGS Middleweight Championship Tournament Winner, and 2005 PRIDE Middleweight Grand Prix Runner-Up.  In submission wrestling, he holds an undefeated record of 13-0, never losing a single point in a match, and is a three-time ADCC Champion.  He has notable wins in both MMA and submission grappling competition over Tito Ortiz, Jeff Monson, Renato Sobral, Vitor Belfort, Mark Kerr, Kazushi Sakuraba, Wanderlei Silva, Dan Henderson, Alistair Overeem, Murilo Rua, Jeremy Horn, Guy Mezger, and Dean Lister.

Guy Mezger: Guy Mezger (born January 1, 1968) is an American martial artist, who competed in professional combat sports including full contact karate, kickboxing, and boxing, but is most recognized as a mixed martial arts (MMA) fighter.  Mezger retired from professional competition on January 25, 2005.  He is associated with Lion's Den and runs their school in Dallas.  Mezger was a champion in mixed martial arts in two different promotions, the UFC and Pancrase.  He holds wins over Tito Ortiz, Masakatsu Funaki, Yuki Kondo, Semmy Schilt, and Minoru Suzuki.

Lion's Den (mixed martial arts): The Lion's Den is a mixed martial arts team and training facility that was based out of Lodi, California and San Diego, California but has recently moved its headquarters to Reno, Nevada.  The team was founded in the early 1990s by UFC Hall of Famer Ken Shamrock, and was the most dominant fight camp in the early UFC.  It featured fighters such as Frank Shamrock, Guy Mezger, Vernon "Tiger" White, Jerry Bohlander, Tra Telligman, Pete Williams, and Mikey Burnett.  The Lion's Den now features many new training facilities, including Lion's Den Arizona, Lion's Den Connecticut, and Lion's Den Reno.

Jerry Bohlander: Jerry Bohlander (born February 12, 1974) is an American former mixed martial artist.  He is most notable for his UFC appearances and was a former UFC champion, winning the first lightweight (under 200 lb) tournament at "UFC 12".  He was a member of the legendary fight team the Lion's Den alongside other notable fighters such as Ken Shamrock, Guy Mezger, and Frank Shamrock.  Bohlander was considered one of the best under 200 lb.  fighters in the world during his time with the UFC.

Semmy Schilt: Sem "Semmy" Schilt (] ; born 27 October 1973) is a Dutch former kickboxer, Ashihara karateka, mixed martial artist, one-time and four-time K-1 World Grand Prix Champion.  He is the only fighter in K-1 history to win the world championship three times in a row, and also shares the record with Ernesto Hoost for most Grand Prixs won, with four.

Masakatsu Funaki: Masakatsu Funaki (船木 誠勝 , Funaki Masakatsu , born March 13, 1969 as Masaharu Funaki) is a Japanese actor, mixed martial artist and professional wrestler, who has previously wrestled in All Japan Pro Wrestling (AJPW), New Japan Pro-Wrestling (NJPW), Pro Wrestling Fujiwara Gumi (PWFG), Newborn UWF, and Wrestle-1 (W-1).  He is also the co-founder of Pancrase, one of the first mixed martial arts organizations and non-rehearsed shoot wrestling promotions (following five years after the inception of Shooto but predating America's Ultimate Fighting Championship).  Funaki was also Pancrase's biggest star; Josh Barnett described him as the "symbol of Japan", Frank Shamrock labeled Funaki "the golden boy" of Pancrase, and Guy Mezger called Funaki "hands down the smartest and most skilled fighter in Pancrase next to Ken Shamrock".

MFC 26: MFC 26: Retribution was a mixed martial arts event held by the Maximum Fighting Championship (MFC) on September 10, 2010 at the River Cree Casino in Enoch, Alberta.  The event was aired live on HDNet with commentators Michael Schiavello, Frank Trigg and Guy Mezger.

Gilbert Ballantine: Gilbert Ballantine (born 14 March 1961) is a retired Dutch kickboxer and a nine times kickboxing world champion.  After his kickboxing career Ballantine also took part in Mixed martial arts competition, winning three Rings Dutch championships.  Ballantine currently lives in Amsterdam and teaches Kickboxing at Ben Rietdijk Sport, Health & Beauty.

Question: Guy Mezger holds wins over which former Dutch kickboxer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fighter_name": {
      "type": "string",
      "description": "The name of the fighter whose wins are being queried."
    },
    "opponent_nationality": {
      "type": "string",
      "description": "The nationality of the opponent."
    },
    "opponent_discipline": {
      "type": "string",
      "description": "The primary combat sport discipline of the opponent."
    },
    "defeated_opponent": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the defeated opponent."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the defeated opponent."
        },
        "achievements": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Notable achievements of the defeated opponent."
        }
      },
      "required": [
        "name",
        "birth_date",
        "achievements"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "fighter_name",
    "opponent_nationality",
    "opponent_discipline",
    "defeated_opponent"
  ],
  "additionalProperties": false
}
