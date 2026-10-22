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
SV St. Georg: SV St. Georg Hamburg is a German association football club playing in Hamburg.  The club was established 3 June 1895 and shares a common origin with "FC Hammonia Hamburg": both sides arose out of the students group Seminarvereinigung Frisch-Auf with "St. Georg" being formed first on the left bank of the Alster River, and "Hammonia" appearing later on the right bank.  Like their brother side, "St. Georg" was a founding member of the German Football Association (Deutscher Fussball Bund or German Football Association) at Leipzig in 1900.  However, while "Hammonia" folded after only a short existence, "St. Georg" still plays today.

Audioslave: Audioslave was an American rock supergroup formed in Los Angeles in 2001.  The four-piece band consisted of Soundgarden lead singer/rhythm guitarist Chris Cornell and Rage Against the Machine members Tom Morello (lead guitar), Tim Commerford (bass/backing vocals), and Brad Wilk (drums).  Critics first described Audioslave as a combination of Soundgarden and Rage Against the Machine, but by the band's second album, "Out of Exile", it was noted that they had established a separate identity.  Audioslave's sound was created by blending 1970s hard rock with 1990s alternative rock.  Moreover, Morello incorporated his well-known, unconventional guitar solos into the mix.  As with Rage Against the Machine, the band prided themselves on the fact that all sounds on their albums were produced using only guitar, bass, drums, and vocals.

Primary rock: Primary rock is an early term in geology that refers to crystalline rock formed first in geologic time, containing no organic remains, such as granite, gneiss and schist as well as igneous and magmatic formations from all ages.  Webster's Revised Unabridged Dictionary published in 1913 provides the following term as used in geology:

Liberty Baptist Church (Grooverville, Georgia): Liberty Baptist Church is a historic church built about 1858 in Grooverville, Georgia.  It was added to the National Register of Historic Places on August 20, 2013.  It is located on Liberty Church Road.  There is a Georgia Historical Commission historical marker at the site.  According to the marker: "In 1841 the Ocklochnee anti-Missionary Baptist Association passed a ruling to dismiss members believing in the 'new fangled institutions of the day.'"  One of the excommunicated sisters joined with others in forming the Liberty Baptist Church.  The church includes a slave gallery.  Freed slaves from the area formed First Elizabeth Church in Grooverville.

Dubstar: Dubstar are an English band, performing dream pop and alternative dance, as well as occasional pop ballads and, on later releases, guitar-laden rock with industrial twists.  The group was formed in 1992 by Steve Hillier and Chris Wilkie in Newcastle-upon-Tyne.  Sarah Blackwood joined in 1993, replacing Hillier on vocals.

Harris, Forbes &amp; Co.: Harris, Forbes & Co. was an investment banking affiliate of Harris Bank incorporated in 1911.  Harris, Forbes firm was acquired by Chase Manhattan Bank in 1930 to form Chase Harris, Forbes.  Just two years later, in 1932, the firm was dissolved after the passage of the Glass–Steagall Act in 1932.  Chase transferred what remained of its securities business to the Bank of Boston's newly formed First Boston Corporation, buttressing that firm's early municipal bond department.

Konstantin Vakulovsky: Captain Konstantin Konstantinovich Vakulovsky (born 28 October 1894, died Summer 1918) was a World War I flying ace credited with six aerial victories.  A major general's son, he volunteered for aviation duty on 8 August 1914, six days after graduating from university.  He taught himself to fly, and became one of Russia's first military pilots on 13 June 1915.  After escaping the fall of the Novogeorgievsk Fortress in a hazardous flight, Vakylovsky flew reconnaissance missions, some through heavy ground fire.  Given command of the newly formed First Fighter Detachment, he became a flying ace credited with six aerial victories.  He died in a flying accident during Summer 1918.

Japp–Maitland condensation: The Japp–Maitland condensation is an organic reaction and a type of Aldol reaction and a tandem reaction.  In a reaction between the ketone 2-pentanone and the aldehyde benzaldehyde catalyzed by base the bis Aldol adduct is formed first.  The second step is a ring-closing reaction when one hydroxyl group displaces the other in a nucleophilic substitution forming an oxo-tetrahydropyran.

Audioslave discography: The discography of Audioslave, an American hard rock band, consists of three studio albums, two extended plays (EPs), fourteen singles, two video albums and ten music videos. Formed in Los Angeles, California in 2001, Audioslave was a supergroup featuring former Soundgarden and Temple of the Dog vocalist Chris Cornell and three former members of Rage Against the Machine – guitarist Tom Morello, bassist Tim Commerford and drummer Brad Wilk.  Signed to Epic and Interscope Records, the band released its self-titled debut album in November 2002, which peaked at number 7 on the US "Billboard" 200.  Supported by five singles, all of which reached the top ten of the "Billboard" Mainstream Rock Songs chart, "Audioslave" was certified triple platinum by the Recording Industry Association of America (RIAA).  The band's first video album, also self-titled, was released in 2003 and reached number 5 on the "Billboard" Top Music Videos chart, receiving a gold certification from the RIAA.

West Bengal Legislative Assembly election, 1967: The West Bengal Legislative Assembly election, 1967 was held in Indian state of West Bengal in 1967 to elect 280 members to the West Bengal Legislative Assembly.  United Front led by Ajoy Mukherjee won majority of seats in the election, and formed first non-Congress government of the state.

Question: Which band was formed first, Dubstar or Audioslave?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_formed_first": {
      "type": "string",
      "description": "The name of the band that was formed first."
    },
    "first_band_formation_year": {
      "type": "integer",
      "description": "The year the first band was formed."
    },
    "second_band_name": {
      "type": "string",
      "description": "The name of the other band in the comparison."
    },
    "second_band_formation_year": {
      "type": "integer",
      "description": "The year the second band was formed."
    },
    "comparison_result": {
      "type": "boolean",
      "description": "True if the first band was indeed formed earlier than the second band."
    }
  },
  "required": [
    "band_formed_first",
    "first_band_formation_year",
    "second_band_name",
    "second_band_formation_year",
    "comparison_result"
  ],
  "additionalProperties": false
}
