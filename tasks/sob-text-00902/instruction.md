{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKaren B. Stewart: Karen Brevard Stewart (born 1952) is an American diplomat who is the current United States Ambassador to the Marshall Islands.  She was nominated by President Barack Obama to be United States Ambassador to the Marshall Islands on November 5, 2015 was confirmed by the U.S. Senate on May 17, 2016.  Stewart also served as United States Ambassador to Belarus from August 14, 2006 to March 12, 2008 and as United States Ambassador to Laos from November 2010 to August 2013.\n\nWilliam F. Hagerty: William Francis Hagerty IV (born August 14, 1959) is an American private equity investor who currently serves as the United States Ambassador to Japan.  He was previously the managing director and co-founder of Hagerty Peterson & Company, a private equity investment firm.  On March 27, 2017, President Donald Trump nominated Hagerty to serve as United States Ambassador to Japan, succeeding Obama appointee Caroline Kennedy.  On July 27, 2017, Vice President Mike Pence administered the oath of office to Hagerty, who became the 42nd United States Ambassador to Japan.\n\nWanda Nesbitt: Wanda L. Nesbitt (born December 7, 1956) is a United States diplomat.  A career Foreign Service officer, she has been appointed U.S Ambassador to several countries.  From January 2002 to August 2004, Nesbitt was the United States Ambassador to Madagascar, the United States Ambassador to Cote d'Ivoire from 2007-2010 and she was appointed United States Ambassador to Namibia on September 24, 2010.  She graduated from the University of Pennsylvania with a degree in international relations and French and also attended the National War College.\n\nTulinabo S. Mushingi: Tulinabo Salama Mushingi (born August 4, 1956) is an American diplomat who currently serves a joint appointment as United States Ambassador to Senegal and United States Ambassador to Guinea-Bissau.  He previously served as the United States Ambassador to Burkina Faso from 2013 to 2016.  He also served in the executive offices of Secretaries of State John F. Kerry and Hillary Clinton.  In February 2017, President Donald Trump nominated Mushingi to serve concurrently as United States Ambassador to Senegal and United States Ambassador to Guinea-Bissau.  Mushingi had originally been nominated for the position by outgoing President Barack Obama in January 2017.  When Trump took office, he withdrew Mushingi's nomination before renominating him for the same position.  He was confirmed by the United States Senate by voice vote on May 18, 2017.\n\nClifford Sobel: Clifford Michael Sobel (born 1949, Brooklyn, New York) is an American business executive, financier, Republican fundraiser, U.S. diplomat and former ambassador.  Most recently, he served as the United States Ambassador to Brazil.  He was nominated for the post by President George W. Bush on May 23, 2006, confirmed by the United States Senate on June 29, 2006, and sworn in by Secretary of State Condoleezza Rice on July 20, 2006.  He presented his credentials to the Brazilian Foreign Ministry on August 2, 2006.  Ambassador Sobel is the 53rd Chief of Mission to Brazil.  He resigned as ambassador in August 2009.  From 2001-05, Sobel was the 62nd United States Ambassador to the Netherlands.  President George W. Bush nominated him on July 3, 2001 and he was sworn in by Secretary of State Colin Powell on November 8, 2001.  On December 5, 2001, he presented his credentials to Her Majesty Queen Beatrix.\n\nHarry K. Thomas Jr.: Harry Keels Thomas Jr. (born June 3, 1956 in the Harlem section of New York City) is an American diplomat and current United States Ambassador to Zimbabwe.  He served as the United States Ambassador to the Philippines from 2010 to 2013.  A former United States Ambassador to Bangladesh (serving from 2003 to 2005) and Director General of the United States Foreign Service (serving from 2007 to 2009), Thomas was designated by US President Barack Obama on November 19, 2009 to replace Kristie Kenney as Ambassador to the Philippines—the first African American to serve at that post.  He was confirmed by the United States Senate on March 19, 2010 and presented his credentials to Philippine president Gloria Macapagal-Arroyo on April 27, 2010 He was then nominated and confirmed as the United States Ambassador to Zimbabwe on October 22, 2015.  He was sworn in on December 8, 2015.\n\nCarissa Phelps: Carissa Phelps (born September 12, 1976) is a Mexican-American author, attorney, and advocate for sexually exploited runaway children and homeless youth.  She is known as the subject of the award-winning documentary, \"Carissa\", directed by David Sauvage and produced by Davis Guggenheim, Chad Troutwine, and Jamie McCourt.  The 2008 film revisits her life as a sexually exploited runaway child living on the streets of Fresno, California.  Having been involved in various petty crimes and probation violations, as well as grand theft auto, she was incarcerated at the CK Wakefield Home for Boys, during their pilot program to integrate girls into the facility as an option to sentencing them to the California Youth Authority.  Teaching herself mathematics and working to overcome numerous rapes, sexual exploitation, and substance abuse and addictions, she eventually graduated with an MBA and a law degree from UCLA.  She is the founder of Runaway Girl, Inc., which advocates for runaway and homeless youth, while providing training for organizations to effectively reach out and address homelessness and human trafficking.  In 2012, her life story was told in the book, \"Runaway Girl: Escaping Life on the Streets, One Helping Hand at a Time\".\n\nJamie McCourt: Jamie D. McCourt (born December 5, 1953) is a businesswoman and investor.  She is the founder and CEO of Jamie Enterprises, and the former co-owner and executive of the Los Angeles Dodgers.  She became the highest-ranking woman in Major League Baseball, appointed first as Vice Chairman of the Dodgers in 2004, then President in 2005, and finally CEO in 2009.  On June 22, 2017, she was nominated as United States Ambassador to Belgium.  On August 2, 2017, President Trump formally withdrew her nomination and instead nominated her as United States Ambassador to France and United States Ambassador to Monaco.\n\nTodd Philip Haskell: Todd Philip Haskell (born 1962) is an American diplomat and career Foreign Service Officer who currently serves as the United States Ambassador to the Republic of the Congo.  Prior to assuming his current position, he served as Deputy Assistant Secretary in the Bureau of African Affairs at the United States Department of State from 2015 to 2017.  In February 2017, President Donald Trump nominated Haskell for the position of United States Ambassador to the Republic of the Congo.  Haskell had originally been nominated for the position by outgoing President Barack Obama in January 2017.  When Trump took office, he withdrew Haskell's nomination before reinstating his nomination.  Haskell was confirmed for the position by the United States Senate on May 18, 2017.\n\nLuis E. Arreaga: Luis E. Arreaga-Rodas (born 1952) is a Guatemalan American diplomat and government official who has been confirmed as the next United States Ambassador to Guatemala.  He previously served as United States Ambassador to Iceland from 2010 until 2013.  In January 2016, he was appointed Principal Deputy Assistant Secretary of State for the Bureau of International Narcotics and Law Enforcement Affairs.  In June 2017, President Donald Trump nominated Arreaga to become the United States Ambassador to Guatemala.  This nomination was confirmed by the U.S. Senate on August 3, 2017.\n\nQuestion: What documentary did the person nominated as United States Ambassador to France on August 2017 produce ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person identified in the question.\"\n    },\n    \"ambassador_nomination\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"nominated_country\": {\n          \"type\": \"string\",\n          \"description\": \"The country for which the person was nominated as ambassador.\"\n        },\n        \"nomination_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date of the ambassadorial nomination.\"\n        }\n      },\n      \"required\": [\n        \"nominated_country\",\n        \"nomination_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"documentary_produced\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the documentary produced by the person.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the person in the production of the documentary.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"ambassador_nomination\",\n    \"documentary_produced\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person identified in the question."
      },
      "ambassador_nomination": {
        "type": "object",
        "properties": {
          "nominated_country": {
            "type": "string",
            "description": "The country for which the person was nominated as ambassador."
          },
          "nomination_date": {
            "type": "string",
            "description": "The date of the ambassadorial nomination."
          }
        },
        "required": [
          "nominated_country",
          "nomination_date"
        ],
        "additionalProperties": false
      },
      "documentary_produced": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the documentary produced by the person."
          },
          "role": {
            "type": "string",
            "description": "The role of the person in the production of the documentary."
          }
        },
        "required": [
          "title",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_name",
      "ambassador_nomination",
      "documentary_produced"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
