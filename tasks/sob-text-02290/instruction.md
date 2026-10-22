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
Arumalai kottai: Arumalai kottai is a village in Thanjuvur, Tamil Nadu, India.  The Original Name of the Village is "Arulmozhi Kottai".  Arulmozhi varman is the name of King Raja cholan.  This village belongs to one of the Vazhanadu in his ruling called ""Kundavai" Vazhanadu"; Kundavai is the name of his Sister "Kundavai Piratti".  Over period of time the village name become Arumalai kottai and the nadu name become "Kulanthai VazhaNadu".

EPRU Stadium: EPRU Stadium, also known by its original name of Boet Erasmus Stadium, was a stadium in Port Elizabeth, South Africa.  The letters "EPRU" in the name represent the Eastern Province Rugby Union, the company behind the stadium's historic primary tenants, the Mighty Elephants.  The original name Boet Erasmus Stadium was named after Boet Erasmus, a former mayor of Port Elizabeth.  The stadium held a capacity of 33,852 people and served primarily as a venue for rugby union matches but also hosted a number of football fixtures.

Bashir Ahmed Sarki: Bashir Sarki, full name Haji Bashir Ahmed Sarki, was born in the small town of Thul on 13 March 1951, and belongs to the udi village in Jacobabad (Sindhi: جیکب آباد) Sindh, Pakistan.  Its geographical coordinates are 28° 12' 0" North, 68° 47' 0" East and its original name (with diacritics) is Udi.  He is considered to be one of the most powerful Feudal Lords of the district and belongs from the historic Sarki dynasty of Sindh, which was formerly known as the Sharqi empire of Jaunpur.  He holds a title of Vadera, meaning Lord, which he inherited from his forefathers, who were once the rulers of Jaunpur, which is now a part of India.  He is reported to be the key person behind the major political decisions taken in the locality.

SS El Oriente: SS "El Oriente was a cargo ship built in 1910 for the Morgan Line, a subsidiary of the Southern Pacific Company.  During World War I, she was known as USS "El Oriente" (ID-4504) in service with the United States Navy.  At the end of war, she reverted to her original name of SS "El Oriente".  During World War II she was chartered by the International Committee of the Red Cross (ICRC) as SS "Henri Dunant (sometimes also spelled Henry Dunant), but reverted to her original name of SS "El Oriente" at the end of the charter.

Symbiote (comics): The Symbiotes (originally known as the Klyntar) are a fictional race of amorphous extraterrestrial symbiotes appearing in American comic books published by Marvel Comics.  The Symbiotes bond with their hosts, creating a symbiotic bond through which creates a single entity.

Carnage (comics): Carnage (Cletus Kasady) is a fictional supervillain appearing in American comic books published by Marvel Comics, usually as an enemy of Spider-Man.  The character first appeared as Kasady in "The Amazing Spider-Man" #344 (March 1991) and as Carnage in "The Amazing Spider-Man" #360.  Carnage was created by writer David Michelinie and artists Erik Larsen and Mark Bagley, based on elements of the precursor character Venom.  Along with Venom, the character belongs to a race of amorphous extraterrestrial parasites known as the Symbiotes.  In 2009, Carnage was ranked as IGN's 90th Greatest Comic Book Villain of All Time.

Sakura Kinomoto: Sakura Kinomoto (木之本 桜 , Kinomoto Sakura ) is the main protagonist and title character of Clamp's manga series "Cardcaptor Sakura".  In the English anime adaptation by Nelvana of the series, "Cardcaptors", her name is changed to Sakura Avalon, though it was changed back to her original name in the dub of the 2nd film by Bang Zoom!  Entertainment.  For the alternative English dub by Omni Productions, her original name was fully kept, making it more faithfully closer to the original Japanese version.  For all Japanese-language productions of the anime (including movies, audio CDs, and video games), Sakura is voiced by Sakura Tange.  For the Nelvana English-language dub production, she is voiced by Carly McKillip through "Cardcaptors" and the first movie.  She is voiced in the second movie by Kari Wahlgren.  For the alternative English dub produced by Omni Productions to air on Animax Asia, she was voiced by Andrea Kwan.

Uncle Slam: Uncle Slam was an American crossover thrash band from Los Angeles, California, formed in 1984 under the name The Brood.  They were influenced by punk rock bands of the 1980s like Suicidal Tendencies (which featured some of the members of Uncle Slam and The Brood), D.R.I., Corrosion of Conformity, Black Flag and the Circle Jerks, as well as heavy metal bands like Black Sabbath, Iron Maiden, Slayer and Motörhead.  Many of their songs are about politics, rebel themes, death, pain and violence.  Uncle Slam has released four studio albums (one was recorded under their original name) and four demo tapes (one was also recorded under their original name).  The band broke up in 1995 but in 2010 they reissued their 1988 album "Say Uncle" on CD for the first time.

Plus (TV channel): Plus was a digital channel run by Granada Sky Broadcasting.  It was launched on 1 October 1996 under the original name of Granada Plus, and during its availability it underwent successive rebrands as G Plus, G+ and then simply Plus.  However, it remained widely referred to by the public at large by its original name.  On 1 November 2004, it was permanently closed down by ITV plc in an attempt to bring its replacement, ITV3, on Sky.

Ganja, Azerbaijan: Ganja (Azerbaijani: "Gəncə" ] ) is Azerbaijan's second largest city with a population of around 325,200.  It was named Elisabethpol (Russian: Елизаветпо́ль , "Yelizavetpol"; ] ) in the Russian Empire period.  The city regained its original name, Ganja, in 1920 during the first part of its incorporation into the Soviet Union.  However, its name was changed again in 1935 to Kirovabad (Russian: Кироваба́д ; ] ) and retained that name through most of the rest of the Soviet period.  In 1989, during Perestroika, the city regained its original name.

Question: What was the original name of the race that Carnage belongs to?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the character in question."
    },
    "race_details": {
      "type": "object",
      "properties": {
        "current_name": {
          "type": "string",
          "description": "The current common name of the race."
        },
        "original_name": {
          "type": "string",
          "description": "The original name of the race."
        }
      },
      "required": [
        "current_name",
        "original_name"
      ],
      "additionalProperties": false
    },
    "publisher": {
      "type": "string",
      "description": "The publisher of the comic books."
    }
  },
  "required": [
    "character_name",
    "race_details",
    "publisher"
  ],
  "additionalProperties": false
}
