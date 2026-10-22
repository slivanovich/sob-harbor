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
Alice Dudley, Duchess of Dudley: Alice Dudley, Duchess of Dudley (née Leigh; 1579 – 22 January 1669), also known as Duchess Dudley, was the second wife of the explorer Sir Robert Dudley.  In 1605, after giving birth to seven daughters, she was abandoned by her husband, who went into exile in Tuscany, remarried, and eventually sold his English estates.  In 1644, by way of reparation for her losses, King Charles I created Alice Dudley a duchess in her own right "for her natural life", the dukedom thus created not being heritable.

Princess Victoria Melita of Saxe-Coburg and Gotha: Princess Victoria Melita of Saxe-Coburg and Gotha and Edinburgh , later Grand Duchess Victoria Feodorovna of Russia (25 November 1876 – 2 March 1936) was the third child and second daughter of Alfred, Duke of Saxe-Coburg and Gotha, and Grand Duchess Maria Alexandrovna of Russia.  She was a granddaughter of Queen Victoria of the United Kingdom and Emperor Alexander II of Russia.

List of accolades received by The Young Victoria: "The Young Victoria" is a 2009 period drama film directed by Jean-Marc Vallée and written by Julian Fellowes.  It centered on the early life and reign of Queen Victoria, including her relationship with her husband, Prince Albert.  The film starred Emily Blunt and Rupert Friend among a large ensemble cast.  Martin Scorsese, Graham King, and Sarah, Duchess of York served as its producers.  A GK Films production, "The Young Victoria" was distributed by Momentum Pictures in the United Kingdom and by Apparition in the United States.  Its world premiere was held on 5 February 2009 at the 59th Berlin International Film Festival while its UK premiere was held in London's Leicester Square on 3 March.  The film was screened throughout 2009 and early 2010 at film festivals in Toronto, Sudbury, Ontario, Chicago, Hamptons, New York, Vermont, San Francisco, Denver, and San Joaquin, California.  "The Young Victoria"' s theatrical release occurred on 6 March 2009 in the UK; it was released in a limited capacity in the US on 18 December 2009, and opened nationwide on Christmas Day.  It earned a worldwide gross of $27,409,889.

Grand Duchess Maria Kirillovna of Russia: Grand Duchess Maria Kirillovna of Russia, (2 February 1907 – 25 October 1951) was the eldest daughter of Grand Duke Kirill Vladimirovich of Russia and Grand Duchess Victoria Feodorovna.  She was born in Coburg when her parents were in exile because their marriage had not been approved by Tsar Nicholas II.  She was generally called "Marie," the French version of her name, or by the Russian nickname "Masha."  The family returned to Russia prior to World War I, but was forced to flee following the Russian Revolution of 1917.

Emich Kyrill, Prince of Leiningen: Emich was born at Coburg, Weimar Republic, the first child of Karl, Prince of Leiningen (1898–1946), (son of Emich, 5th Prince of Leiningen and Princess Feodore of Hohenlohe-Langenburg) and his wife, Grand Duchess Maria Kirillovna of Russia (1907–1951), (daughter of Cyril Vladimirovich, Grand Duke of Russia and Princess Victoria Melita of Saxe-Coburg and Gotha).  Through his mother, he was a descendant of Queen Victoria and Tsar Alexander II.  Through his father, he was a descendant of the Vasa kings of Sweden and of both of Queen Victoria's half-siblings, Carl, Prince of Leiningen and The Princess of Hohenlohe-Langenburg.  As a result, Emich was the first descendant of all three of Victoria, Duchess of Kent's children.

Kensington System: The Kensington System was a strict and elaborate set of rules designed by Victoria, Duchess of Kent, along with her attendant, Sir John Conroy, concerning the upbringing of the Duchess's daughter, the future Queen Victoria.  It is named after Kensington Palace in London, where Victoria resided with her mother prior to acceding the throne.

The White Duchess: The White Duchess is a life sized (194 x 130 cm) oil-on-canvas painting by the Spanish artist Francisco Goya, completed in 1795 and now in the collection of the Duchess of Alba, Madrid.  It portrays María Cayetana de Silva, 13th Duchess of Alba, and is one of a number of portraits Goya painted of her around this time, and is usually compared alongside the similarly sized but tonally very different "Black Duchess", which was painted two years later, just after her husband, José Álvarez de Toledo died aged 39.  The duke and duchess were highly placed, cultivated and well-regarded members of the 1790s Spanish Court.

Charles Wellesley, 9th Duke of Wellington: Arthur Charles Valerian Wellesley, 9th Duke of Wellington, (born 19 August 1945) is a British aristocrat and politician.  He has served as Conservative Party Member of the European Parliament (1984–1989) for Surrey West and currently sits as a hereditary peer in the House of Lords since 2015.

Natalia Grosvenor, Duchess of Westminster: Natalia Ayesha Grosvenor, Duchess of Westminster ("née" Phillips; born 8 May 1959) is the widow of Gerald Grosvenor, 6th Duke of Westminster.  The Duchess will assume the style of Dowager Duchess only upon the marriage of her son.  At the time of her husband's succession to the title, there were four Duchesses of Westminster, the current Duchess, Sally Grosvenor, Duchess of Westminster, Anne Grosvenor, Duchess of Westminster and Viola Grosvenor, Duchess of Westminster.

Princess Antonia, Duchess of Wellington: Princess Antonia of Prussia, Duchess of Wellington, Duchess of Ciudad Rodrigo, Princess of Waterloo, Duchess of Victoria, (born 28 April 1955), is a great-granddaughter of Wilhelm II, German Emperor and the wife of Charles Wellesley, 9th Duke of Wellington.

Question: What did the husband of Duchess Victoria do for a living? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "duchess_full_name": {
      "type": "string",
      "description": "The full name and titles of the Duchess mentioned in the question."
    },
    "husband_full_name": {
      "type": "string",
      "description": "The full name and titles of the Duchess's husband."
    },
    "husband_political_roles": {
      "type": "array",
      "description": "A list of political roles or occupations held by the husband.",
      "items": {
        "type": "object",
        "properties": {
          "role_title": {
            "type": "string",
            "description": "The title of the political role."
          },
          "start_year": {
            "type": "integer",
            "description": "The year the role started."
          },
          "end_year": {
            "type": "integer",
            "description": "The year the role ended, if applicable."
          },
          "is_current": {
            "type": "boolean",
            "description": "Indicates if the role is currently held."
          }
        },
        "required": [
          "role_title",
          "start_year",
          "is_current"
        ],
        "additionalProperties": false
      }
    },
    "primary_occupation_summary": {
      "type": "string",
      "description": "A concise summary of the husband's primary occupation as requested in the question."
    }
  },
  "required": [
    "duchess_full_name",
    "husband_full_name",
    "husband_political_roles",
    "primary_occupation_summary"
  ],
  "additionalProperties": false
}
