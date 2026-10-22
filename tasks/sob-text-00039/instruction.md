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
Law and Disorder in Philadelphia: Law and Disorder in Philadelphia (also titled Killadelphia) is a 2008 British documentary by Louis Theroux.

Lebanese nationality law: Lebanese nationality law is the law governing the acquisition, transmission and loss of Lebanese citizenship.  Lebanese citizenship is the status of being a citizen of the Republic of Lebanon and it can be obtained by birth or naturalisation.  The Lebanese nationality is transmitted by paternity (father) (see Jus sanguinis).  Therefore, a Lebanese man who holds Lebanese citizenship can automatically confer citizenship to his children and foreign wife (only if entered in the Civil Acts Register in the Republic of Lebanon).  Under the current law, descendants of Lebanese emigrants can only receive citizenship from their father and women cannot pass on citizenship to their children or foreign spouses.  On 12 November 2015, the Parliament of Lebanon approved a draft law that would allow "foreigners of Lebanese origin to get citizenship", the Minister of Foreign Affairs and Emigrants Gebran Bassil announced on 5 May 2016 the beginning of the implementation of citizenship law for Lebanese diaspora.

Louis Theroux: Louis Sebastian Theroux ( ; born 20 May 1970) is an English documentary filmmaker and broadcaster who holds dual British and American citizenship.

Carina Lau: Carina Lau Kar-ling (born 8 December 1965) is a Chinese actress and singer.  She holds citizenship from China (Hong Kong) and Canada.  Lau started her acting career in TVB, before going on to achieve success in films.  She was especially notable in the 1980s for her girl-next-door type roles in films.

Eddie Peng: Eddie Peng Yu-Yan (; born 24 March 1982) is a Canadian actor, singer, and model.  Peng moved to Vancouver, British Columbia, Canada at the age of thirteen.  In 2000, he graduated from Sir Winston Churchill Secondary School.  Subsequently, he was admitted into the University of British Columbia and majored in economics, but later dropped out to begin his acting career.  He holds citizenship in both Taiwan and Canada.

Peter Friis Johansson: Peter Friis Johansson (born 1983) is a Swedish classical pianist who also holds citizenship of Denmark.  He won first prize in the Alaska International Piano-e-Competition in 2014.

Ryan Alosio: Ryan Alosio is an American actor and visual artist who holds citizenship in both Ireland and the U.S.  The son of an Irish mother and Italian father, Alosio spent eight years in boarding schools, three in military academy.  He graduated with honors from the Interlochen Arts Academy and continued his studies at Northwestern University in Chicago, studying film and journalism and New York University where he majored in dramatic writing in the Tisch School of the Arts.  He currently plays 'Miles Farber' on the Jim Carrey produced Showtime series, "I'm Dying Up Here", and has portrayed an eclectic mix of characters in stage, film and television productions opposite such actors as Hugh Laurie, Elijah Wood, Jeff Goldblum, Kiefer Sutherland, Judith Light, Gary Sinise, John Hawkes, Patrick Dempsey, and Jason Alexander.  Alosio appears in and voices multiple national Ad campaigns for Dodge, Mountain Dew, Carl's Jr. and Nissan, as well as animated characters for Warner Bros., Honda, Japanese Anime, Cartoon Network and multiple industry leading gaming franchises such as game of the year and BAFTA Award winning "Fallout 4", "Titanfall 2", Marvel's "The Amazing Spiderman 2", and "Rise of the Tomb Raider".  Alosio is a gallery shown and sold abstract painter and published photographer with work featured in noted publications such as Rizzoli International's "Modern Americana", architectural publication "Modern Magazine" and "The New York Times Magazine".  He was the singer/songwriter of the alt-rock band, "blackradio", performing throughout Los Angeles at The Viper Room, The Hard Rock, The Mint and The Los Angeles Music Awards.  Alosio passionately rides and has built and customized multiple vintage motorcycles and award winning classic muscle cars.  He is an animal lover and environmentalist and makes his home in Los Angeles, California.

Al Bandar report: The Al Bander report [Al Bandar] refers to an alleged political conspiracy by certain government officials in Bahrain to foment sectarian strife and marginalize the majority Shia community in the country.  The conspiracy was allegedly led and financed by Ahmed bin Ateyatalla Al Khalifa, Minister of Cabinet Affairs and head of the Civil Informatics Organization and member of the Al Khalifa royal family.  The allegations were revealed in September 2006, in a 240-page document produced by the Gulf Centre for Democratic Development, and authored by Dr Salah Al Bandar, an adviser to the Cabinet Affairs Ministry.  Following the distribution of the report, Bahraini police forcibly deported Dr Al Bandar to the United Kingdom, where he holds citizenship.

Radoslav Nesterović: Radoslav "Rašo" Nesterović (Serbian Cyrillic: , Slovene: "Radoslav "Rašo" Nesterovič" ), usually referred to in English as Rasho Nesterovic (born May 30, 1976), is a retired Slovenian professional basketball player.  He holds citizenship in both Slovenia and Greece.  In the NBA he played for the Minnesota Timberwolves, San Antonio Spurs, Indiana Pacers, and Toronto Raptors.  Nesterović retired in 2011.

German nationality law: German nationality law is the law governing the acquisition, transmission and loss of German citizenship.  The law is based on a mixture of the principles of "jus sanguinis" and "jus soli".  In other words, one usually acquires German citizenship if a parent is a German citizen, irrespective of place of birth, or by birth in Germany to parents with foreign nationality if certain requirements are fulfilled.  Naturalisation is also possible for foreign nationals after six to eight years of legal residence in Germany.  However, non-EU and non-Swiss citizens must usually renounce their old citizenship before being naturalised in Germany.  Citizens of other EU countries and of Switzerland usually can keep their old citizenship.  Some EU countries do not allow dual citizenship even with other EU countries.  German citizens wanting to acquire a non-EU or non-Swiss citizenship and to maintain their German citizenship must apply for a permission ("Beibehaltungsgenehmigung") before acquiring the other citizenship, or they will automatically lose their German citizenship when they acquire the foreign citizenship.  For details, see section "Dual citizenship."

Question: The filmmaker for Law and Disorder in Philadelphia holds citizenship where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "filmmaker_name": {
      "type": "string",
      "description": "The name of the documentary filmmaker."
    },
    "documentary_title": {
      "type": "string",
      "description": "The title of the documentary in question."
    },
    "citizenship_status": {
      "type": "string",
      "description": "Describes the nature of the filmmaker's citizenship (e.g., 'dual')."
    },
    "citizenship_countries": {
      "type": "array",
      "description": "A list of countries where the filmmaker holds citizenship.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "filmmaker_name",
    "documentary_title",
    "citizenship_status",
    "citizenship_countries"
  ],
  "additionalProperties": false
}
