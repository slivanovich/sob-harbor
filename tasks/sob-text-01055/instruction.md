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
Cartman's Mom Is a Dirty Slut: "Cartman's Mom Is a Dirty Slut" is the first season finale of the American animated television series "South Park".  It originally aired on Comedy Central in the United States on February 25, 1998.  The episode is the highest viewed episode in the entire "South Park" series, with 6.4 million views.  It is part one of a two-episode story arc, which concluded with "Cartman's Mom Is Still a Dirty Slut".  The episode follows Eric Cartman, one of the show's child protagonists, becoming curious about the identity of his father.  He discovers that his father is most likely a man his mother had sexual intercourse with during an annual party called "The Drunken Barn Dance".  Meanwhile, his friends Stan, Kyle and Kenny participate on "America's Stupidest Home Videos", after filming Cartman playing in his yard with plush toys.

Ya`fūr: Ya`fūr (also variously rendered as Ya'foor, Ya'four, `Ufayr, `Ofayr and so on, meaning "Deer" in Arabic) was a donkey used as a mount by the Islamic prophet Muhammad, who was said to have often ridden it bareback.  There are many tales of this donkey but the most common would be that the donkey is recorded to have been a gift from the Byzantine governor of Egypt some time between 628 and 632 AD (8–11 AH).  According to an Islamic tradition, it had the power of speech and told Muhammad that it was the last of a line of donkeys ridden by prophets and was a descendant of the donkey ridden by Jesus in his triumphal entry into Jerusalem, which was also called Ya`fūr.  The tradition holds that Ya`fūr committed suicide in despair after Muhammad died by throwing itself into a well, though these accounts are held to be unreliable in hadith studies.  In the centuries after Muhammad's death, the donkey's name and symbolism was repeatedly adopted by Islamic religious figures and rulers.

Al-Insān al-Kāmil: In Islamic theology, al-Insān al-Kāmil (Arabic: الإنسان الكامل‎ ‎ ) also rendered as "Insān-i Kāmil" (Persian/Urdu: انسان کامل ) and "İnsan-ı Kâmil" (Turkish), is a term used as an honorific title to describe the prophet Muhammad.  The phrase means "the person who has reached perfection."  It is an important concept in Islamic culture of the prototype human being, pure consciousness, one's true identity, to be contrasted with the material human who is bound by one's senses and materialism.  The term was originally used by Sunni Sufis and is still used by them, however it is also used by Alawis and Alevis.  This idea is based upon a hadith, which was used by Ibn Arabi, that states about Prophet Muhammad, 'I was a prophet when Adam was between water and clay'.

MyMFB: MyMFB (previously MillatFacebook) is a Muslim-oriented social networking website.  It was launched in May 2010 in response to a controversial group on Facebook entitled "Everybody Draw Mohammed Day" and Pakistan's block of Facebook in response.

Everybody Draw Mohammed Day: Everybody Draw Mohammed Day (or "Draw Mohammed Day") was a 2010 event in support of artists threatened with violence for drawing representations of the Islamic prophet Muhammad.  It stemmed from a protest against censorship of the American television show "South Park" episode "201", led by the show's distributor Comedy Central, in response to death threats that had been made against some of those responsible for two segments broadcast in April 2010.  A drawing representing Mohammed was posted on the Internet on April 20, 2010 with a message suggesting that "everybody" create a drawing depicting Mohammad on May 20 in support of free speech.

Kurt Westergaard: Kurt Westergaard (born Kurt Vestergaard, 13 July 1935) is a Danish cartoonist who created the controversial cartoon of the Islamic prophet Muhammad wearing a bomb in his turban.  This cartoon was the most contentious of the 12 Jyllands-Posten Muhammad cartoons, which met with strong reactions from Muslims worldwide, including Western countries.  Since the drawing of the cartoon, Westergaard has received numerous death threats and been a target of assassination attempts.  As a result, he is under constant police protection.

201 (South Park): "201" is the sixth episode of the fourteenth season of "South Park", and the 201st overall episode of the series.  It originally aired on Comedy Central in the United States on April 21, 2010.  The episode continued multiple storylines from the previous episode, "200", in which a group of angry celebrities demand South Park produce the Muslim prophet Muhammad.  In "201", a superhero-like group of religious figures team up to save South Park from the celebrities and their monster Mecha-Streisand, while Eric Cartman learns the true identity of his father.

Cartoon Wars Part II: "Cartoon Wars Part II" is the fourth episode in the tenth season of the American animated television series "South Park".  The 143rd episode of the series overall, it first aired on Comedy Central in the United States on April 12, 2006.  After "Cartoon Wars Part I", it is the second part of a two-episode story-arc, which focuses on Cartman's efforts to get the television series "Family Guy" cancelled, by exploiting fears of retaliation by Muslims to an impending "Family Guy" episode in which the Islamic prophet Muhammad will appear, in violation of some interpretations of Muslim law.  Kyle instead urges the president of the network airing "Family Guy", Fox, to air the episode in an exercise of free speech.

Maqbara: The Arabic word Maqbara (مقبرة "mausoleum"; "plural": مقابر Maqâbir) is derived from the word Qabr, which means grave.  Though maqbara refers to the graves of all Muslims, it refers especially to the graves (Raula or Rauza) of religious figures or Waliyullahs considered to have dedicated their life to Islam, striving to be true Muslims and training others to follow Islam as preached by the Islamic prophet Muhammad.

History of Hajj: The History of the Hajj encompasses a period starting from the time of Abraham through the establishment of the Islamic Hajj by Islamic prophet Muhammad, to the present-day hajj where millions of Muslims perform their pilgrimage annually.  In Islamic tradition, pilgrimage was introduced during the time of prophet Ibrahim (Abraham).  Upon God's command, he built Kaaba which became the destination of pilgrimage.  For the pagan Arabs in the Pre-Islamic Arabia, Kaaba was still the center of their worshiping.  The present pattern of the Islamic Hajj was established by Prophet Muhammad, around 632 CE, who made reforms to the pre-Islamic pilgrimage of the pagan Arabs.  During the medieval times, pilgrims would gather in chief cities like Basra, Damascus, and Cairo to go to Mecca in groups and caravans comprising tens of thousands of pilgrims.

Question: Everybody Draw Mohammed Day (or "Draw Mohammed Day") was a 2010 event in support of artists threatened with violence for drawing representations of the Islamic prophet Muhammad, it stemmed from a protest against censorship of the American television show "South Park" which specific episode, in response to death threats that had been made against some of those responsible for two segments broadcast, in which episode, a superhero-like group of religious figures team up to save South Park from the celebrities and their monster Mecha-Streisand, while Eric Cartman learns the true identity of his father?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "episode_title": {
      "type": "string",
      "description": "The title of the South Park episode."
    },
    "episode_identifiers": {
      "type": "object",
      "properties": {
        "season_number": {
          "type": "integer",
          "description": "The season number of the episode."
        },
        "overall_episode_number": {
          "type": "integer",
          "description": "The overall episode number in the series."
        },
        "original_air_date": {
          "type": "string",
          "format": "date",
          "description": "The original air date of the episode."
        },
        "network": {
          "type": "string",
          "description": "The television network that originally aired the episode."
        }
      },
      "required": [
        "season_number",
        "overall_episode_number",
        "original_air_date",
        "network"
      ],
      "additionalProperties": false
    },
    "main_storylines": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key plot points or storylines featured in the episode."
    },
    "related_protest_event": {
      "type": "object",
      "properties": {
        "event_name": {
          "type": "string",
          "description": "The name of the event related to the episode's censorship."
        },
        "reason_for_protest": {
          "type": "string",
          "description": "The specific reason for the protest related to this episode."
        }
      },
      "required": [
        "event_name",
        "reason_for_protest"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "episode_title",
    "episode_identifiers",
    "main_storylines",
    "related_protest_event"
  ],
  "additionalProperties": false
}
