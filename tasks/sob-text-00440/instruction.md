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
Abdallah bin Laden: Abdallah bin asjad bin Mohammed bin Awad bin Laden (Arabic: عبدالله بن أسامة بن محمد بن عوض بن لادن‎ ‎ ; born c. 1989) is the son of Osama bin Laden and Osama's first wife Najwa Ghanem.  He is not to be confused with Osama bin Laden's half-brother Abdullah bin Laden (born in 1966) or the older Sheikh Abdullah bin Laden, who died in 2002 at age 75.

Hamza bin Laden: Hamza bin Osama bin Mohammed bin Awad bin Laden (Arabic: حمزة بن أسامة بن محمد بن عوض بن لادن‎ ‎ ; born c. 1989 in Jeddah, Saudi Arabia), better known as Hamza bin Laden or "Hamza Laden", is a son of Osama bin Laden.  His father, as well as his brother Khalid, were killed in the 2011 Navy SEAL raid.

Nasser al-Bahri: Nasser al-Bahri (1972 – December 26, 2015), also known by his "kunya" or "nom de guerre" as Abu Jandal – "father of death", was a member of al-Qaeda in Afghanistan from 1996 to 2000.  He gave his bayat (secret oath of allegiance) to Osama bin Laden in 1998, an experience he describes in detail in his memoir.  He was in al-Qaeda for four years, first as one of bin Laden's twelve bodyguards, and then as head of Osama bin Laden's security detail.  A citizen of Yemen born in Saudi Arabia, Al-Bahri was radicalized in his teens by dissident Saudi Ulemas and participated in clandestine political activities which were funded in part by people trafficking.  Having determined to become a jihadist he went first to Bosnia and then, briefly, to Somalia before arriving in Afghanistan in 1996 in the hope of joining Al-Qaeda, which he soon did.  After four years, al-Bahri became "disillusioned", largely because bin Laden consolidated al-Qaeda's relationship with the Taliban by giving his bayat to its leader, Mullah Omar, but also because he had married and become a father.

Bin Laden (song): "Bin Laden" is a hip hop song by Immortal Technique, Mos Def and DJ Green Lantern.

Hamida al-Attas: Hamida Ibrahim (Arabic: حميدة ابراهيم‎ ‎ , "Ḥamīdah Ibrahīm"; born 1934) born Hamida Ibrahim (Arabic: Hamida Ibrahim‎ ‎ , " Hamida Ibrahim"), is the mother of Osama bin Laden.  She came from a Syrian family of two brothers and another sister.  She married Mohammed bin Awad bin Laden in Latakia in 1956 and moved to Saudi Arabia with her husband.  She was the eleventh wife of Mohammed bin Awad bin Laden.  Her husband had at least 22 wives but divorced many, having only four wives at once, in accordance with Muslim law.  It has been reported that she was a concubine rather than wife of Mohammed bin Awad bin Laden.  She was more cosmopolitan than Mohammed's first three Wahhabi Saudi wives.

Mos Def: Yasiin Bey ( ) (born Dante Terrell Smith; December 11, 1973), best known by his stage name Mos Def ( ), is an American hip hop recording artist, actor and activist from Brooklyn, New York City, New York.  Best known for his music, Mos Def embarked on his hip hop career in 1994, alongside his siblings in the short-lived rap group Urban Thermo Dynamics (UTD), after which he appeared on albums by Da Bush Babees and De La Soul.  He subsequently formed the duo Black Star, alongside fellow Brooklyn-based rapper Talib Kweli, and they released their eponymous debut album in 1998.  He was featured on the roster of Rawkus Records and in 1999 released his solo debut, "Black on Both Sides".  His debut was followed by "The New Danger" (2004), "True Magic" (2006) and "The Ecstatic" (2009).  The editors at About.com listed him as the 14th greatest emcee of all time on their "50 greatest MC's of our time" list.

Manhunt: The Search for Bin Laden: Manhunt: The Search for Bin Laden is a 2013 documentary film directed by Greg Barker that explores the Central Intelligence Agency's investigation of Osama bin Laden, starting from 1995 until his death in 2011.  It premiered on HBO on May 1, 2013, two years after the mission that killed bin Laden.  The documentary features narratives by many of the CIA analysts and operatives who worked over a decade to understand and track bin Laden, and includes archival film footage from across Washington, D.C., Pakistan, Saudi Arabia and elsewhere in the Middle East.  It also features extensive and rarely seen footage of Al-Qaeda training and propaganda videos, including video suicide notes from various terrorists who later worked as suicide bombers.

Tere Bin Laden: Tere Bin Laden (English: Your Bin Laden ) is a 2010 Bollywood satire film produced by Walkwater Media and written and directed by Abhishek Sharma.  The film stars Pakistani pop singer Ali Zafar in the lead role as an ambitious young reporter, who, in his desperation to migrate to the United States, makes a fake Osama bin Laden video using a look-alike, and sells it to TV channels.  Osama bin Laden was played by Pradhuman Singh.  The film is a spoof on Osama Bin Laden as well as a comic satire on America's war against terror and the realities of the post-9/11 world.  The film was released worldwide, except the United States, on 16 July 2010.

Osama bin Laden death conspiracy theories: The death of Osama bin Laden gave rise to various conspiracy theories, hoaxes, and rumors.  These include the ideas that bin Laden had been dead for years, or is still alive.  Doubts about bin Laden's death were fueled by the U.S. military's supposed disposal of his body at sea, the decision to not release any photographic or DNA evidence of bin Laden's death to the public, the contradicting accounts of the incident (with the official story on the raid appearing to change or directly contradict previous assertions), and the 25-minute blackout during the raid on bin Laden's compound during which a live feed from cameras mounted on the helmets of the U.S. special forces was cut off.

Omar bin Laden: Omar bin Osama bin Mohammed bin Awad bin Laden (Arabic: عمر بن أسامة بن محمد بن عوض بن لادن‎ ‎ , "ʿUmar bin ʾUsāmah bin Muḥammad bin ʿAwaḍ bin Lādin"; born 1981), better known as Omar bin Laden, is one of the sons of Osama bin Laden and his first wife and first cousin Najwa Ghanem (see Bin Laden family).  He is the fourth-eldest son among 20 children of Osama bin Laden.  Older reports have described Omar and his brother Abdallah bin Laden as nephews or cousins of Osama bin Laden.

Question: What genre was the song Bin Laden by Mos Def part of?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "artist": {
      "type": "string",
      "description": "The primary artist associated with the song."
    },
    "genre": {
      "type": "string",
      "description": "The musical genre of the song."
    }
  },
  "required": [
    "song_title",
    "artist",
    "genre"
  ],
  "additionalProperties": false
}
