{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nChicago Opera Company: The Chicago Opera Company was a grand opera company in Chicago, organized from the remaining assets of the bankrupt Chicago City Opera Company, that produced six seasons of opera at the Civic Opera House from 1940 to 1946 (excluding 1943).  Artistic directors included Carlo Peroni (1941-1942) and Fausto Cleva (1944-1946), and until 1945 Fortune Gallo was general manager.  After the war, when consumer goods became more abundant and people spent less money on entertainment, interest in opera collapsed and the company went bankrupt.  Rather than try to re-organize, the remaining assets were given to the largest creditor, the landlord of the Civic Opera House, Household finance, who then paid off the other remaining creditors.  After the final collapse of an opera company that had been re-organized five times, there was no resident Chicago opera company until the founding of the Lyric Opera in 1954.  One of the original group of organizers was Max Rabinoff.\n\nHillhouse Opera Company: Hillhouse Opera Company is a U.S. non-profit opera company that performs in the New Haven area of Connecticut.  Founded in 2008 by Victoria Leigh Gardner, Nicole Rodriguez and Jim Coatsworth, and based in New Haven, Connecticut, Hillhouse Opera Company has offered productions of \"Alcina\", \"Don Giovanni\", \"Faust\", \"Così fan tutte\" and \"La Bohème\".  It also stages opera scenes programs, master classes and concert series.\n\nJames Westman: James Westman (born September 16, 1972) is a Canadian baritone known for his interpretation of the Verdi, Puccini and bel canto operatic repertoire, and particularly his signature role of Germont in \"La traviata\", which he has sung in over 150 performances, with opera companies such as San Francisco Opera, Houston Grand Opera, Pittsburgh Opera, Florida Grand Opera, Graz Opera, Santa Fe Opera, Chicago Lyric Opera, Opéra de Montréal, Los Angeles Opera, Grand Théâtre de Bordeaux, Canadian Opera Company, Boston Lyric Opera, Cologne Opera, Vancouver Opera, English National Opera, San Diego Opera, Dallas Opera, Utah Opera, and Opera Theatre of St. Louis.  On January 29, 2011 Westman created the lead role of Sandy Keith In the world premiere of Bramwell Tovey's The Inventor.  In 2017 he played Sir John A. MacDonald in Harry Somers's Louis Riel for the Canadian Opera Company's tribute to Canada's 150th celebrations.  As a recitalist, he has performed for the Marilyn Horne Foundation, Aldeburgh Connection, Aldeburgh Festival, Musikverein, Wigmore Hall, Queen Elizabeth Hall, Morgan Library & Museum, Koerner Hall, Carnegie Hall, Saito Kinen Festival in Japan, Stratford Summer Music, British Broadcasting Corporation, and the Canadian Broadcasting Corporation.  Westman first came to attention at the age of twelve when he was the first boy soprano to perform and record Mahler \"4th Symphony\" with Benjamin Zander and the Boston Philharmonic Orchestra in 1984.  Westman is regularly featured as the Anthem singer for the Toronto Maple Leafs and numerous other NHL franchises.  Four of Westman's recordings have been nominated for a Juno Award.  Two recordings nominated for a Grammy Award.\n\nMax Maretzek Italian Opera Company: The Max Maretzek Italian Opera Company (sometimes referred to as the Italian Opera Company, the Italian Grand Opera Company, or Academy of Music Opera Company) was a touring American opera company that performed throughout the United States from 1849-1878.  The first major opera company in Manhattan and one of the first important companies in the United States, it had a long association with the Academy of Music in New York City where it presented an annual season of opera from 1854 until the company's demise in 1878 There the company performed the United States premieres of \"Rigoletto\", \"Il trovatore\", and \"La traviata\" among other works.\n\nAmerican Opera Company: The American Opera Company was the name of four different opera companies active in the United States.  The first company was a short-lived opera company founded in New York City in February, 1886 that lasted only one season.  The second company was based out of Rochester, New York and was active from the mid-1920s up until 1930 when it went bankrupt not too long after the Wall Street Crash of 1929.  The third opera company was a short lived company located in Trenton, New Jersey that was active in 1937.  The fourth and last opera company was actively performing in Philadelphia from 1946 through 1950.\n\nWilliam Tell (opera): Guillaume Tell (English: William Tell , Italian: Guglielmo Tell ) is a French opera in four acts by Gioachino Rossini to a libretto by Étienne de Jouy and Hippolyte Bis.  Based on Friedrich Schiller's play \"William Tell,\" which drew on the William Tell legend, the opera was Rossini's last, although he lived for nearly forty more years.  Fabio Luisi said that Rossini planned for \"William Tell\" to be his last opera even as he composed it.  The overture, in four sections and featuring a depiction of a storm as well as a vivacious finale, the \"March of the Swiss Soldiers,\" is often played.\n\nChicago City Opera Company: The Chicago City Opera Company was a grand opera company in Chicago, organized from the remaining assets of the bankrupt Chicago Grand Opera Company, that produced four seasons of opera at the Civic Opera House from 1935 to 1939 before it too succumbed to financial difficulties.  It was succeeded by the Chicago Opera Company.\n\nLithuanian Opera Company of Chicago: The Lithuanian Opera Company of Chicago was founded by Lithuanian emigrants in 1956, and presents operas in Lithuanian.  It celebrated fifty years of existence in 2006, and operates as a not-for-profit organization.  It is noteworthy for performing the rarely staged Rossini's \"William Tell\" (1986) and Ponchielli's \"I Lituani\" (1981, 1983 and 1991), and also for contributing experienced chorus singers to the Lyric Opera of Chicago.\n\nPhiladelphia Lyric Opera Company: The Philadelphia Lyric Opera Company was an American opera company located in Philadelphia, Pennsylvania that was active between 1958 and 1974.  The company was led by a number of Artistic Directors during its history, beginning with Aurelio Fabiani.  Other notable Artistic Directors include Julius Rudel and Anton Guadagno (1966–1972).  The company produced between four and six of their own operas every year in addition to sponsoring numerous traveling productions from the New York City Opera.  In 1975 the company merged with the Philadelphia Grand Opera Company but retained its original name.  With the combined resources of both companies, the Philadelphia Lyric Opera Company began producing higher quality productions with name artists such as Luciano Pavarotti, Joan Sutherland, Roberta Peters, Montserrat Caballé, and others.  For the bicentennial year 1976, the company commissioned famed opera composer Gian Carlo Menotti to create a new opera.  The work, The Hero, premiered on June 1, 1976.  In 1980, the company artistically reorganized to form the Opera Company of Philadelphia.\n\nPhiladelphia Grand Opera Company: The Philadelphia Grand Opera Company was the name of four different American opera companies active at the Academy of Music in Philadelphia, Pennsylvania during the twentieth century.  The last and best known of the four was founded in November 1954 with the merger of the Philadelphia Civic Grand Opera Company and the Philadelphia La Scala Opera Company.  That company in turn merged with the Philadelphia Lyric Opera Company in 1975 to form the Opera Company of Philadelphia.  Of the three earlier companies, only one lasted beyond one season; a company founded in 1926 which later became associated with the Curtis Institute of Music in 1929.  That company closed its doors in 1932 due to financial reasons during the Great Depression.\n\nQuestion: The Lithuanian Opera Company of Chicago stages an opera which is based on a play by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"opera_company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the opera company.\"\n    },\n    \"staged_opera\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the opera staged by the company.\"\n        },\n        \"composer\": {\n          \"type\": \"string\",\n          \"description\": \"The composer of the opera.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"composer\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"source_play\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the play the opera is based on.\"\n        },\n        \"author\": {\n          \"type\": \"string\",\n          \"description\": \"The author of the play.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"author\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"opera_company_name\",\n    \"staged_opera\",\n    \"source_play\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "opera_company_name": {
        "type": "string",
        "description": "The name of the opera company."
      },
      "staged_opera": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the opera staged by the company."
          },
          "composer": {
            "type": "string",
            "description": "The composer of the opera."
          }
        },
        "required": [
          "title",
          "composer"
        ],
        "additionalProperties": false
      },
      "source_play": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the play the opera is based on."
          },
          "author": {
            "type": "string",
            "description": "The author of the play."
          }
        },
        "required": [
          "title",
          "author"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "opera_company_name",
      "staged_opera",
      "source_play"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
