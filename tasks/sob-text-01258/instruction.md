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
List of role-playing game publishers: This is a list of companies that have produced tabletop role-playing games, listed in order of the year that the company published its first role-playing game-related product (game, supplement, or magazine).  Also listed is the years the company was active, and a list of notable role-playing games the company has produced.  This list makes note of the first edition of each game which a company published, and does not try to list subsequent editions of the same game published by the same company.

Fast and Furious (1939 film): Fast and Furious is a 1939 American mystery comedy film directed by Busby Berkeley.  The film stars Franchot Tone and Ann Sothern as Joel and Garda Sloane, a crime-solving married couple who are also rare book dealers.  It is the last of a Metro-Goldwyn-Mayer trilogy, along with "Fast Company" (1938) and "Fast and Loose" (1939).  However, different actors played the couple each time.

Alan Webber: Alan Webber (born September 18, 1948, St. Louis, Missouri) is an American entrepreneur, writer and progressive Democrat who unsuccessfully ran for Governor of New Mexico in 2014.  Following his run for Governor, Webber founded One New Mexico, a solution-oriented nonprofit aimed at advancing New Mexico's economic outlook, nurturing entrepreneurship and innovation and connecting New Mexicans statewide.  In 1981, Webber worked as an employee of the Harvard Business School, where he went on to serve for six years as managing editor and editorial director of the "Harvard Business Review".  In 1995, Webber co-founded the technology business magazine, "Fast Company", where he was named Adweek's Editor of the Year in 1999.  In 2000, investors sold "Fast Company" for $360 million, which was at the time the second highest price ever paid for a U.S. magazine.

Toby Press: Toby Press was an American comic-book company that published from 1949 to 1955.  Founded by Elliott Caplin, brother of cartoonist Al Capp and himself an established comic strip writer, the company published reprints of Capp's "Li'l Abner" strip; licensed-character comics starring such film and animated cartoon properties as John Wayne and Felix the Cat; and original conceptions, including romance, war, Western, and adventure comics.  Some of its comics were published under the imprint Minoan.  Some covers bore the logo ANC, standing for American News Company, at the time the country's largest newsstand distributor.

Gutsoon! Entertainment: Gutsoon!  Entertainment, Inc. is a now defunct publisher of English translated manga.  The company, headquartered in Encino, Los Angeles, served as the US subsidiary of Coamix, which was founded by Nobuhiko Horie and manga artist Tsukasa Hojo.  The company published the English manga anthology "Raijin Comics", a U.S. equivalent to the Japanese "Weekly Comic Bunch" and published many of the same titles ("Fist of the Blue Sky" and "City Hunter"), as well titles from other magazines such as the Japanese "Weekly Shōnen Jump".  "Raijin Comics" began as a weekly magazine with its first issue (dated December 18, 2002), but switched to being a monthly publication beginning with its 36th issue (dated September 2003).  Gutsoon!  also published a companion magazine to "Raijin Comics", titled "Raijin Game & Anime" (originally called "Fujin Magazine"), which lasted only 20 issues before being merged into the pages of "Raijin Comics".  The collected volumes of "Raijin Comics" titles were published under the "Raijin Graphic Novels" imprint.  Raijin Comics also has a mascot called "Raijin Maru".  Before the company's fall they were also planning to make a shōjo manga magazine called "Smile Magazine".

Fast and Loose (1939 film): Fast and Loose is a 1939 American thriller film directed by Edwin L. Marin and starring Robert Montgomery, Rosalind Russell and Reginald Owen.  It is a sequel to the 1938 film "Fast Company" and was followed the same year by "Fast and Furious".  In each film, different actors played the crime-solving couple.

Fast Company (1938 film): Fast Company is a 1938 mystery film starring Melvyn Douglas and Florence Rice as married rare-book dealers who try to solve a murder case.  It is based on the novel of the same name by "Marco Page" (Harry Kurnitz).  It was followed by two 1939 films featuring the fictional couple, "Fast and Loose" and "Fast and Furious", though they were played by different actors in each.  Apparently, cinema distributors were complaining about the time lag between The Thin Man movies, so Metro-Goldwyn-Mayer started this trilogy featuring married amateur sleuths.  To avoid confusion with a 1953 MGM film of the same title, "Fast Company" was rechristened "Rare Book Murder" for television.

Fast Company (magazine): Fast Company is a monthly American business magazine published in print and online that focuses on technology, business, and design.  It publishes 10 print issues per year.  Robert Safian has been the editor-in-chief since 2007, having previously worked at "Fortune", "Time", and "Money".  "Fast Company" is owned by Mansueto Ventures and is headquartered in New York, New York.

Playboy: Playboy is an American men's lifestyle and entertainment magazine.  It was founded in Chicago in 1953, by Hugh Hefner and his associates, and funded in part by a $1,000 loan from Hefner's mother.  Notable for its centerfolds of nude and semi-nude models (Playmates), "Playboy" played an important role in the sexual revolution and remains one of the world's best-known brands, having grown into Playboy Enterprises, Inc., with a presence in nearly every medium.  In addition to the flagship magazine in the United States, special nation-specific versions of "Playboy" are published worldwide.

April Summers: Summers began modelling in 2007 with CXLondon, a fashion company in the UK.  Since then, she has appeared in numerous publications.  The work of the English model can be found in many notable magazines such as "GQ, GQ Mexico" "and "FHM"."  Besides the UK, the model made her US debut in 2012, when she was featured in an issue of "Maxim".  April Summers rose to prominence when she first appeared as a "Playboy" Playmate for "Playboy" France's gold issue in September 2010, where she posed for a 12-page spread.  Ever since, it has been a landslide for the English model, as she went on to appear in "Playboy Italy, Playboy Hungary, Playboy Lithuania", "Playboy Poland, Playboy Spain, Playboy Macedonia", "Playboy Argentina, Playboy Slovenia, Playboy Thailand, Playboy Slovakia", and "Playboy Mexico".  However, her international success does not stop there, the model is constantly being published in top Italian magazines ever since she rose to fame in Italy by announcing that she is a fan of the world known team Inter Milan.  April was interviewed by "Playboy" in October 2010 for their website "The Smoking Jacket".  and is the face of The Golden Handcuff Co.  In November 2011, she released her first official calendar.

Question: Are Playboy and Fast Company published in the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the magazines being compared."
    },
    "magazine_details": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the magazine."
          },
          "country_of_publication": {
            "type": "string",
            "description": "Country where the magazine is published."
          }
        },
        "required": [
          "name",
          "country_of_publication"
        ],
        "additionalProperties": false
      },
      "description": "Details for each magazine including its publication country."
    },
    "are_published_in_same_country": {
      "type": "boolean",
      "description": "True if both magazines are published in the same country, false otherwise."
    },
    "common_country_of_publication": {
      "type": "string",
      "description": "The country where both magazines are published, if applicable."
    }
  },
  "required": [
    "magazine_names",
    "magazine_details",
    "are_published_in_same_country",
    "common_country_of_publication"
  ],
  "additionalProperties": false
}
