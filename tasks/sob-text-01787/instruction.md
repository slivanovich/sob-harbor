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
Miss Universe 1967: Miss Universe 1967, the 16th Miss Universe pageant, was held on 15 July 1967 at the Miami Beach Auditorium in Miami Beach, Florida, USA.  Sylvia Hitchcock of USA was crowned by Margareta Arvidsson of Sweden at the end of the event, This was Bob Barker's first Miss Universe pageant as host.

Renate Cerljen: Renate Veronica Cerljen (born March 26, 1988 in Staffanstorp, Sweden) is the first ever winner of the Miss Universe Sweden pageant which she won on June 6, 2009.  Cerljen represented Sweden at the Miss Universe 2009 pageant on the Bahamas on August 23, 2009 and placed in the Top 15.  Renate was the first non-winner of the Miss Sweden pageant since 1952 to represent Sweden at Miss Universe since Miss Sweden lost its rights to crown a contestant for Miss Universe earlier in 2009.  Cerljen was also the first delegate from Sweden at the international final since 2006 when Josephine Alhanko placed in the Top 20.  Miss Universe 1984 winner Yvonne Ryding was among the judges in the final which crowned Cerljen as winner.  By making the Top 15 Cerljen became Sweden's 29th semifinalist at the Miss Universe pageant overall.  In May 2010 Cerljen placed fifth in the Miss Beauty of the World pageant in China.  Cerljen was a judge at the Miss Sinergy competition for breast cancer in 2009 as well as 2010 which is an annual pageant made by the Sinergy group, held at the House of Sweden in Washington DC, United States.

Brook Lee: Brook Antoinette Mahealani Lee (born January 8, 1971 in Pearl City, Hawaii), known as Brook Lee, is an American actress, TV Host, model and beauty queen who was crowned Miss Hawaii USA 1997, Miss USA 1997, and Miss Universe 1997.

Señorita México: Señorita México was the name of a national beauty pageant in Mexico, celebrated since 1952.  After 2005, the pageant changed its name to "Miss Mexico".  From 1952 to 1994, was the official pageant responsible for sending the country's representatives to the Miss Universe, Miss World, Miss International and other international pageants.  After the crowning of Lupita Jones, as the country's first Miss Universe, a dispute between Miss Jones and the pageant organizers over overdued prizes, led to a break of the longtime association between the pageant and the broadcast network Televisa.  When the pageant moved to another network TV Azteca, a competing pageant called "Nuestra Belleza México" was created, later directed by Miss Jones with the sponsorship of the Televisa TV Network.  in 1994 Señorita México lost the bid to Nuestra Belleza México to be the official pageant for the Miss Universe pageant.  Later Nuestra Belleza México also obtained the rights of sending Mexico's representatives to Miss World and Miss International.  However, the "Miss Mexico" pageant still sends representatives to other international pageants.  The trade name Señorita Mexico was trademarked in the United States, by Venezuelan Entrepreneur Adan S. Perez CEO of The Miss Mexico Organization with headquarters in Las Vegas Nevada who produces The Señorita Mexico U.S. beauty pageant.  He developed a franchise system in every state of The Union to bring girls from all over the United States to compete in national beauty event which takes place every year in Las Vegas.  Adan Perez has been producing the national competition Señorita Mexico U.S in Las Vegas, since the year of 2003.

Andrea Stelzer: Andrea Stelzer (born c. 1965) was a South African beauty queen who also represented Germany in the Miss Universe pageant.  In 1985, Stelzer was Miss South Africa and slated to be a delegate to the Miss Universe pageant, but due to anti-apartheid demonstrations withdrew from the competition.  In 1989, she was Germany's representative to the Miss Universe 1989.

Yendi Phillips: Yendi Amira Phillipps (born September 8, 1985) is a Jamaican TV Host, model and beauty queen who the winner of the Miss Jamaica World 2007 beauty pageant, as well as the Miss Jamaica Universe 2010 pageant.  She represented Jamaica at the Miss World 2007 contest held in Sanya, China and at Miss Universe 2010 held at the Mandalay Bay Resort and Casino, Las Vegas, Nevada, U.S. on August 23, 2010, where she finished as the first runner up to Ximena Navarrete of Mexico.  After Miss Universe Phillipps appeared in commercials for brands such as Toyota.

Marigona Dragusha: Marigona Dragusha (born 23 September 1990) also known as Gona Dragusha is a Kosovar model and beauty queen who placed as the 2nd runner-up at the Miss Universe 2009 pageant, only behind the eventual winner, Venezuela's Stefanía Fernández, and the 1st runner-up Ada de la Cruz from the Dominican Republic.  Dragusha won her national title, Miss Universe Kosovo, on 4 April 2009.  Besides her native Albanian language, Marigona speaks English and Spanish, in which she announced on air before the Miss Universe pageant: she learned the language entirely from watching Spanish-speaking "novelas" (soap operas). She is the first openly lesbian Miss Kosovo.

Jackeline Rodríguez: Jackeline Rodríguez Streffeza (born January 12, 1972) is a Venezuelan model and beauty queen who was the official representative of her country to the 1991 Miss Universe pageant held in Las Vegas, Nevada on May 17, 1991, where she was one of Top 6 finalists.  Rodríguez was not a titleholder of the Miss Venezuela pageant.  That year, the 1991 Miss Venezuela pageant was moved to September, thus taking place after the 1991 Miss Universe pageant.  Rodríguez was ultimately chosen by Osmel Sousa to represent Venezuela at Miss Universe.

Miss Universe 1997: Miss Universe 1997, the 46th Miss Universe pageant, was held on May 16, 1997 at the Miami Beach Convention Center in Miami Beach, Florida.  Brook Lee of the United States won the competition and was crowned by Alicia Machado of Venezuela.  Seventy-four delegates competed in this year.  One of the contestants, Nafisa Joseph, is no longer alive.  This was the last edition of Miss Universe where the winner was seated on the stage during the crowning ceremony.

Shandi Finnessey: Shandi Ren Finnessey (born June 9, 1978, in Florissant, Missouri) is an American actress, model, TV host and beauty queen.  She is best known for winning the Miss USA title, as Miss Missouri USA.  She previously held the title of Miss Missouri 2002 and competed in Miss America, where she won a preliminary award.  She placed as first runner-up at the Miss Universe 2004 competition.  She is one of three women to have been both Miss Missouri USA and Miss Missouri and the only Missourian to have been Miss USA.  Her first runner-up finish at Miss Universe was the best placement in the 2000s and was the best United States placement between Brook Mahealani Lee's Miss Universe 1997 competition victory and Olivia Culpo's Miss Universe 2012 pageant win.

Question: The 46th Miss Universe pageant was won by this American actress, TV Host, model and beauty queen who was born in which city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "pageant_details": {
      "type": "object",
      "properties": {
        "edition_number": {
          "type": "integer",
          "description": "The edition number of the Miss Universe pageant."
        },
        "year": {
          "type": "integer",
          "description": "The year the pageant was held."
        }
      },
      "required": [
        "edition_number",
        "year"
      ],
      "additionalProperties": false
    },
    "winner_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the Miss Universe winner."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the winner."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions or roles held by the winner."
        },
        "birth_location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city where the winner was born."
            },
            "state_or_country": {
              "type": "string",
              "description": "The state or country where the winner was born."
            }
          },
          "required": [
            "city",
            "state_or_country"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "nationality",
        "professions",
        "birth_location"
      ],
      "additionalProperties": false
    },
    "answer_birth_city": {
      "type": "string",
      "description": "The city where the winner was born, directly answering the question."
    }
  },
  "required": [
    "pageant_details",
    "winner_details",
    "answer_birth_city"
  ],
  "additionalProperties": false
}
