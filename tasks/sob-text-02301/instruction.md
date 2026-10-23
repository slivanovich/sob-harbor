{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLegal Entanglement: Legal Entanglement is a 2002 Hong Kong legal drama television series produced by TVB and starring Hacken Lee, Kenix Kwok, Michael Tse and Elaine Ng.\n\nMiss Bangladesh USA: Miss Bangladesh US (Formerly known as Miss Bangladesh USA) is a Beauty pageant in United States for Bangladeshi Americans.  It is the national pageant that elects the Bangladesh representative to Miss Asia Pacific International and Miss Earth.  Miss Bangladesh USA is emerged as the first pageant for Bangladeshi women in almost two decades and is the first organization to be sending a Bangladeshi representative to Miss Asia Pacific International and Miss Earth.  The current titleholder for Miss Bangladesh US is Marjana Chowdhury of New York.\n\nMiss Asia Pageant: ATV Miss Asia Pageant formerly Miss Asia Pageant (亞洲小姐競選), was an annual Hong Kong-based beauty pageant organized and broadcast by Asia Television (ATV).  Originating in 1985 as a local Hong Kong pageant, the contest went on hiatus from the 2000 through 2003, and was re-branded as an Asian pageant in 2004, with contestants spanning the continent of Asia.  The pageant ceased to exist with the shutdown of its organizer, ATV.\n\nLeonora Jiménez: Leonora Jiménez Monge (born 1983 in Santa Ana, Costa Rica) is a Costa Rican beauty pageant titleholder and the original winner of 2005 Miss Asia Pacific International.  She was dethroned because of her participation in Miss World 2005 and the Miss Asia Pacific title was passed to the 1st runner up, Evgeniya Lapova of Russia.  Monge did not place among the semifinalists in Miss World.\n\nElaine Ng Yi-Lei: Elaine Ng (born 23 September 1972), sometimes credited as Elaine Wu, is an actress and was the winner of Miss Asia 1990.\n\nAnukriti Gusain: Anukriti Gusain (Hindi: , born 25 March 1994) is an Indian model, television host and presenter of Planet Bollywood News.  Gusain is crowned Miss Asia Pacific World India 2014 and represented India at Miss Asia Pacific World 2014 an International beauty pageant and finished as \"4th Runner Up\".  She is winner of Femina Miss India Delhi 2013 Crown and Bride Of The World India 2013.  She made a come back to pageantry in 2017, when she won Femina Miss India Uttarakhand 2017 and she represented her home state Uttarakhand among top 30 finalists under the new format of Femina Miss India 2017 pageant She is appointed as Miss Grand India 2017 and will represent India at the minor pageant Miss Grand International 2017 which will be held in Vietnam.\n\nATV Miss Asia Pageant 2011: ATV Miss Asia Pageant 2011, was the 23rd Miss Asia Pageant, which began on 19 January 2012.  The pageant slogan was \"Beauties, Gathered in the Water.\"  For the first time, the organizers created a separate event for all contestants of Chinese descent from mainlain China, Hong Kong, Canada, the US, and Brazil into a semi-final, the results of whom competed with ten contestants of other Asian races.  Michelle Feng of Beijing, China was the winner.\n\nWorarat Suwannarat: Worarat Suwannarat, also known as Emma Suwannarat, Thai: , (born Emma Masterson, January 22, 1977 in Thailand) is a Thai actress, model, host, and the Miss Asia Pacific 1997 titleholder.  She was the first runner up in the 1997 Miss Thailand pageant.  She hosted talk show Sawasdee Bangkok and was Tourism Authority Thailand country ambassador.  Emma was born in Bangkok, Thailand to an Irish father and a Thai mother.  She graduated from Chulalongkorn University, Thailand and from the University of Cambridge, United Kingdom, with a Master of Philosophy.  She represented Thailand at the 1997 Miss Asia Pacific pageant held in Davao City, Philippines and won the competition becoming the third Thai woman ever to capture this prestigious title.  Despite being raised in Ireland, she is fluent in Thai.\n\nMiss Asia Pacific World: Miss Asia Pacific World is a yearly beauty pageant.  There have been a number of controversies with the pageant, and the first three winners have been stripped of their titles.  In 2011, its first winner, Jung Eun A was \"dethroned\" after allegations of \"automatic top-ranking placements in exchange for sex\" by organisers.  British model Amy Willerton fled the competition after lack of food and alleged sexual harassment from organisers.  The 2014 Miss Asia Pacific World, May Myat Noe from Burma, was crowned on 31 May 2014 but was dethroned after three months.\n\nSrishti Rana: Srishti Rana is an Indian model and a beauty pageant titleholder.  She participated in Miss India Universe (Miss Diva) 2013 and won the title of Miss India Asia Pacific.  She went on to represent India at Miss Asia Pacific World 2013 Title in October 2013 which took place in Seoul, Korea.  She emerged as the winner of Miss Asia Pacific World title beating 49 other contestants from different countries.  She also won the best national costume round for which she depicted the national bird of India The Peacock.\n\nQuestion: Which cast member of Legal Entanglement was the winner of Miss Asia 1990?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"tv_series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series.\"\n    },\n    \"tv_series_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the television series was produced or released.\"\n    },\n    \"pageant_winner\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the cast member who won the pageant.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the pageant winner.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"pageant_won\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the beauty pageant won.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the pageant was won.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"tv_series_name\",\n    \"tv_series_year\",\n    \"pageant_winner\",\n    \"pageant_won\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "tv_series_name": {
        "type": "string",
        "description": "The name of the television series."
      },
      "tv_series_year": {
        "type": "integer",
        "description": "The year the television series was produced or released."
      },
      "pageant_winner": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the cast member who won the pageant."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the pageant winner."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "pageant_won": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the beauty pageant won."
          },
          "year": {
            "type": "integer",
            "description": "The year the pageant was won."
          }
        },
        "required": [
          "name",
          "year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "tv_series_name",
      "tv_series_year",
      "pageant_winner",
      "pageant_won"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
