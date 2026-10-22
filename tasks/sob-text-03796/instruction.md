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
Luta Livre: Luta Livre (] "freestyle fighting") is a Brazilian martial art created by Euclydes "Tatu" Hatem.  in Rio de Janeiro.  Primarily a mixture of catch wrestling and judo, there is also striking with the hands, feet, knees and elbows.  Notable practitioners include Marco Ruas, Ebenezer Fontes Braga, Johil de Oliveira, Alexandre Franca Nogueira, Renato Sobral and José Aldo.

Brian Warren: Brian Warren (born June 5, 1974) is an American mixed martial arts fighter from San Bernardino, California.  Warren has fought in many organizations including K-1, King of the Cage, Strikeforce, Kage Kombat, Pangea, and Bellator.  Warren has fought notable title holders such as Cung Le, Jason "Mayhem" Miller, Jeremy Horn, Jake Shields, and other known fighters such as TUF alum Jared Rollins, Justin Levens, Nate Loughran, Karo Parisyan, and Tiki Ghosn.  Warren won a 2nd place medal in 2003 and 3rd place medal in 2006 in the advanced men's division of Grapplers Quest.

Kiyoshi Tamura: Kiyoshi Tamura (田村潔司 , "Tamura Kiyoshi" , born December 17, 1969 in Okayama, Okayama) is a Japanese middleweight professional wrestler and mixed martial artist.  Once a student of legendary pro wrestlers Billy Robinson, Nobuhiko Takada and Akira Maeda, Tamura is known for his skill in catch wrestling as well as his ability to deliver exciting professional wrestling bouts.  He has competed in some form or another for the following organizations: Universal Wrestling Federation, UWF International, Fighting Network RINGS, K-1, PRIDE, and U-STYLE, his own promotion, often fighting much larger opponents.  In mixed martial arts, he holds notable victories over Renzo Gracie, Jeremy Horn, Ikuhisa Minowa, Masakatsu Funaki and Kazushi Sakuraba.

Ricardo Arona: Ricardo Arona (] ; born July 17, 1978) is a retired Brazilian mixed martial artist.  He has competed in PRIDE Fighting Championships and RINGS in his mixed martial arts career, and was a member of Brazilian Top Team.  He is the former RINGS Middleweight Champion, as well as the 2001 RINGS Middleweight Championship Tournament Winner, and 2005 PRIDE Middleweight Grand Prix Runner-Up.  In submission wrestling, he holds an undefeated record of 13-0, never losing a single point in a match, and is a three-time ADCC Champion.  He has notable wins in both MMA and submission grappling competition over Tito Ortiz, Jeff Monson, Renato Sobral, Vitor Belfort, Mark Kerr, Kazushi Sakuraba, Wanderlei Silva, Dan Henderson, Alistair Overeem, Murilo Rua, Jeremy Horn, Guy Mezger, and Dean Lister.

Renato Sobral: Renato da Cunha Sobral (] ; born September 7, 1975), also known as "Babalu", is a retired Brazilian wrestler and mixed martial artist, and former Strikeforce Light Heavyweight Champion.  Sobral previously fought in the Ultimate Fighting Championship, where he posted a 6–4 record and has also competed for Bellator, RINGS, Jungle Fight, Cage Rage, Affliction, and ONE FC.  He is the Head Instructor of Babalu's Iron Gym Cerritos and has a Luta Livre black belt.  He is also a Brazilian jiu-jitsu black belt under Carlos Gracie Jr.  In his prime he was considered one of the top fighters in the world and defeated the likes of former Welterweight UFC Champion Robbie Lawler, former Light Heavyweight UFC Champion Shogun Rua, former Heavyweight UFC Champion Maurice Smith, along with former title contenders Chael Sonnen, Elvis Sinosic, and Jeremy Horn.

Zaza Tkeshelashvili: Zaza "Grom" Tkeshelashvili (born March 19, 1965) is a Georgian retired Freestyle wrestling Olympic competitor (100 kg) for Georgia in 1996 Olympic Games Atlanta and mixed martial artist.  He formerly competed in the Heavyweight (MMA) division, most of which he fought with Fighting Network RINGS where he was known as Zaza Grom.  He lost his last fight at Rings Lithuania – Bushido Rings 2 against Volk Han on August 5, 2001.  He holds notable wins over Volk Han and Travis Fulton, and has fought Bobby Hoffman and Renato Sobral.  His brother Koba Tkeshelashvili is also mixed martial artist and has competed in RINGS.

Jeremy Horn (singer): Jeremy Horn is a contemporary Christian music artist, songwriter, and guitarist.

Renato Aragão: Antônio Renato Aragão (born January 13, 1935, in Sobral, Ceará), nicknamed Didi is a Brazilian comedian actor, producer, and writer.  He is best known for his leading role in the television series "Os Trapalhões".

Jeremy Horn: Jeremy Graham Horn (born August 25, 1975) is an American mixed martial artist currently competing in the Middleweight division.  Although Horn is perhaps best known for fighting in smaller American promotions, he has also competed in some of the premiere mixed martial arts organizations around the world including the UFC, WEC, PRIDE, Bellator, Pancrase, the IFL, King of the Cage, and the International Fighting Championships (IFC).  Horn is the former King of the Cage Light Heavyweight Champion.  Horn has also competed in the Heavyweight and Light Heavyweight divisions.

Miletich Fighting Systems: Miletich Fighting Systems (MFS) is a mixed martial arts (MMA) training organization.  It is recognized as an excellent training camp.  It has been the training camp for fighters such as Matt Hughes, Tim Sylvia, Jens Pulver, Robbie Lawler, and Jeremy Horn.  MFS is widely regarded as one of the most successful MMA camps of all time.

Question: who is older Jeremy Horn or Renato Sobral ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fighter_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first fighter."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the first fighter in YYYY-MM-DD format."
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "fighter_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second fighter."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the second fighter in YYYY-MM-DD format."
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "older_fighter_name": {
      "type": "string",
      "description": "The name of the fighter who is older."
    },
    "age_comparison_result": {
      "type": "string",
      "description": "A statement comparing the ages of the two fighters."
    }
  },
  "required": [
    "fighter_1",
    "fighter_2",
    "older_fighter_name",
    "age_comparison_result"
  ],
  "additionalProperties": false
}
