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
L'Obs: L’Obs ] , previously known as Le Nouvel Observateur (1964-2014), is a weekly French news magazine.  Based in the 2nd arrondissement of Paris, it is the most prominent French general information magazine in terms of audience and circulation.  Its current editor is .

Ursula Gauthier: Ursula Gauthier is a French journalist and sinologist.  Gauthier was a reporter in China for "L'Obs".  In December 2015, her visa was not renewed and she was forced to leave the country after she published an article about Uighurs in Xinjiang which Chinese government officials disapproved of.  A Chinese government Foreign Ministry spokesman suggested Gauthier's article "openly supports terrorist activity, the killing of innocents and has outraged the Chinese public."

Russky Newsweek: Russky Newsweek or "Newsweek Russia" was a Russian language news magazine published in Russia between 2004 and 2010 as the Russian edition of "Newsweek".  It was the first news magazine with a Western origin published in the country.

The Chemical Engineer: The Chemical Engineer is a monthly chemical engineering technical and news magazine published by the Institution of Chemical Engineers (IChemE).  It has technical articles of interest to practitioners and educators, and also addresses current events in world of chemical engineering including research, international business news and government policy as it affects the chemical engineering community.  The magazine is sent to all members of the IChemE and is included in the cost of membership.  Some parts of the magazine are available free online, including recent news and a series of biographies “Chemical Engineers who Changed the World”, although the core and the archive magazine is available only with a subscription.  The online magazine also has freely available podcasts.

NEWS (Austrian magazine): NEWS is an Austrian weekly news magazine published in German and based in Vienna, Austria.  The weekly is the major news magazine in the country.

Alex Mihailovich: Alex Mihailovich is a Canadian broadcaster and is currently a correspondent for RT America.  He was a reporter and news anchor at the now defunct Sun News Network in Canada from 2011 until the station's demise in 2015.  Mihailovich was previously a reporter for Global News Toronto and a correspondent for "", a Canadian investigative news magazine television series which airs nationally on Global TV.  Mihailovich was with CTV Television Network for 5 years which included a role as news anchor at CTV Northern Ontario and as a reporter at CTV Toronto.  Born and raised in Toronto,Canada, he originally attended Carleton University where he was a founding member of the Sigma Pi fraternity chapter there.  He graduated from Seneca College with a radio-television broadcast diploma and has a political science degree from the University of Western Ontario.  Before becoming a journalist, he worked for a United Nations agency in the Balkans from 1995-1999.

Focus (German magazine): Focus (companys's preferred spelling in capital letters) is a German-language news magazine published by Hubert Burda Media.  Established in 1993 as an alternative to the Spiegel weekly news magazine, since 2015 the editorial staff has been headquartered in Germany's capital of Berlin.  Alongside Spiegel and Stern, Focus is one of the three most widely circulated German weeklies.  The concept originated from Hubert Burda and Helmut Markwort, who went from being Editor-in-chief to become publisher in 2009 and since 2017 has been listed in the publication's masthead as Founding Editor-in-chief.  The current Editor-in-chief of Focus as of March 2016 is Robert Schneider.

Mondiaal Nieuws: Mondiaal Nieuws, also called "MO* - Mondiaal Magazine", (meaning "Global News" in English) is a Flemish quarterly alternative news magazine with a special focus on globalization.  The magazine is published as a supplement of the news magazine "Knack" in Brussels, Belgium.

Rock Hard (magazine): Rock Hard (also RockHard) is a German music magazine published in Dortmund, Germany, with other language editions in various countries worldwide, including France, Spain, Brazil/Portugal, Italy and Greece.  The magazine contains reports, interviews, specials, reviews, news and all other content regarding hard rock and heavy metal music.  Next to the German edition of "Metal Hammer" it is the leading magazine for metal and hard rock in Germany.  German news magazine "Der Spiegel" called it the "Zentralorgan" ("Central organ") of the heavy metal fans in Germany, others dubbed it a "Kultzeitschrift" ("cult magazine").  Founded by Holger Stratmann, it has published in Germany more than 300 issues since 1983 and since 1989 has become monthly.  "Rock Hard" magazine is independent from major media companies.  Its slogan is "critical, competent, independent".  Since 1990, the magazine employees have been also organizing the Rock Hard Festival, which is held annually in Gelsenkirchen since 2003 - on the Pentecost weekend.  The festival is streamed by news magazine "Spiegel Online", the internet edition of "Der Spiegel", and by "WDR" television under the "Rockpalast" label.

Sábado (magazine): Sábado is a Portuguese weekly news magazine published in Portugal.  It is the first modern news magazine in the country.

Question: At what frequency the news magazine published in which Ursula Gauthier was reporter in China?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the news magazine."
    },
    "publication_frequency": {
      "type": "string",
      "description": "The frequency at which the magazine is published (e.g., weekly, monthly, quarterly)."
    },
    "journalist_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the journalist."
        },
        "role": {
          "type": "string",
          "description": "The role of the journalist at the magazine."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "magazine_name",
    "publication_frequency",
    "journalist_details"
  ],
  "additionalProperties": false
}
