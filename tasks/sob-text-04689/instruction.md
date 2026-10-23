{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAsian American Hotel Owners Association: The Asian American Hotel Owners Association (AAHOA) is a trade organization that represents Asian American hotel owners in the hospitality industry.  Founded in 1989, AAHOA as of 2006 has more than 8,000 members.\n\nMTV Reality Stars: MTV Reality Stars is India’s first youth sitcom.  It is a season-based fiction TV dramedy (Drama-Comedy) and satire created by Nikhil Taneja that captures the comedy and chaos in the Showbiz industry.  The series also featured cameos by top Bollywood filmmaker Anurag Kashyap and famous Bollywood actors Arshad Warsi and Anand Tiwari.  The 12-episode first season of the show was aired every Saturday on MTV India at 6.30 pm from 16 March 2013 to 1 June 2013.  The humour and the look and feel of the show were in the space of Bollywood movies Delhi Belly and Pyaar Ka Punchnama.\n\nMontvale Hotel: The Montvale Hotel is a boutique hotel in Spokane, Washington.  Originally built in 1899 as an SRO (Single Room Occupancy Hotel), the Montvale Hotel also served Spokane as an apartment building, a brothel, and as a youth hostel during Expo '74 and then was abandoned for 30 years.  It was restored and re-opened in January 2005 as a 36-room boutique hotel, becoming one of Spokane's premier hotels with The Davenport Hotel and the Hotel Lusso.  On August 25, 2015, it was announced that the Montvale Hotel had been acquired by Jerry Dicker's Ruby Hospitality.\n\nTom Mardirosian: Tom Mardirosian (born December 14, 1947) is an Armenian-American actor.  He is known for playing Agamemnon Busmalis in the HBO show \"Oz\" and Agt.  Kristos Koutris in the HBO show \"The Wire\".\n\nDelhi Belly (film): Delhi Belly is a 2011 Indian black comedy film written by Akshat Verma and directed by Abhinay Deo.  It stars Imran Khan, Kunaal Roy Kapur, Vir Das, Poorna Jagannathan and Shenaz Treasurywala.  While the original version was in English, a Hindi dubbed version was also released.  The film is produced by Aamir Khan Productions and IBC Motion Pictures.  The theatrical trailer of the film premiéred with Aamir Khan's \"Dhobi Ghat\" on 21 January 2011 while the film was released on 1 July 2011.  The film was given an 'A' certificate for its profanity and sexual content.  The film was remade in Tamil as \"Settai\".\n\nThe Barrow Group: The Barrow Group is a non-profit Off-Broadway Theatre Company, Acting School and Arts Center located in New York City.  It was founded in 1986 by Lee Brock and Seth Barrish.  The organization has received awards for its productions including a Drama Desk Award, a Lucille Lortel Awards, an OBIE Award, and a nomination for a Pulitzer Prize.  School alumni include Anne Hathaway, Tony Hale, Alison Wright, Michael Stahl-David, Zach Booth and Poorna Jagannathan.\n\nAmerican Hotel and Lodging Association: The American Hotel and Lodging Association (formerly American Hotel and Motel Association, and before that American Hotel Association) is an industry trade group representing organizations of hotel owners.  Its role at various times has included the publication of hotel directories, market research, support of standardisation efforts, public or political advocacy for the interests of hotel owners and the establishment or promotion of training programmes and facilities for hotel personnel.\n\nRoom 104: Room 104 is an American television anthology series created by Jay and Mark Duplass.  The series, ordered by and airing on HBO, debuted on July 28, 2017.  The series is set in a single room of an American hotel, exploring characters who pass through it in each episode.  Each episode is a different genre with some episodes more comical in nature and some more dramatic and some with horror and crime themes.\n\nPoorna Jagannathan: Poorna Jagannathan is an American actress and producer.  She is best known for her portrayal of Safar Khan in HBO's Emmy nominated show, The Night Of\", \"as well as playing the unconventional lead in the Bollywood film \"Delhi Belly\".  She also initiated and produced the play \"Nirbhaya\", written and directed by Yael Farber, which dealt with breaking the silence around sexual violence.  Her play won the '2013 Amnesty International Award' and was called by \"The Telegraph\" as the \"One of the most powerful pieces of theater you'll ever see\".  Jagannathan was featured among the top 10 in Femina magazine's \"India's 50 most beautiful women\" in 2012 and in 2014, she was named among the top 50 most powerful women in India.  She was most recently a series regular on Gypsy, a Netflix original series, and part of the ensemble cast for HBO's new anthology series, Room 104, by the Duplass brothers.\n\nAshraful Haque (actor): Ashraful Haque (3 November 1969 — 17 February 2015) was an Indian actor who mainly appeared in Hindi films and was popularly known for his work in \"Talaash\" (2012), \"Delhi Belly\" (2014) and \"Manjhi - The Mountain Man\" (2015).  He also appeared in \"Black Friday\", \"Company\", \"Deewar\", \"Fukrey\", \"Jungle\", and \"Raavan\" .  He was a graduate of the National School of Drama.\n\nQuestion: Poorna Jagannathan, who appeared in \"Delhi Belly,\" stars in which HBO show set in a single room of an American hotel?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"show_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the HBO show.\"\n    },\n    \"network\": {\n      \"type\": \"string\",\n      \"description\": \"The television network the show airs on.\"\n    },\n    \"show_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of television series (e.g., anthology series).\"\n    },\n    \"setting_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"location_type\": {\n          \"type\": \"string\",\n          \"description\": \"The general type of location where the show is set.\"\n        },\n        \"specific_setting\": {\n          \"type\": \"string\",\n          \"description\": \"The specific setting within the location.\"\n        }\n      },\n      \"required\": [\n        \"location_type\",\n        \"specific_setting\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actress_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress.\"\n        },\n        \"role_in_show\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the actress's role in the identified show.\"\n        },\n        \"known_for_film\": {\n          \"type\": \"string\",\n          \"description\": \"A film the actress is known for, as mentioned in the context or question.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_in_show\",\n        \"known_for_film\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"show_name\",\n    \"network\",\n    \"show_type\",\n    \"setting_details\",\n    \"actress_information\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "show_name": {
        "type": "string",
        "description": "The name of the HBO show."
      },
      "network": {
        "type": "string",
        "description": "The television network the show airs on."
      },
      "show_type": {
        "type": "string",
        "description": "The type of television series (e.g., anthology series)."
      },
      "setting_details": {
        "type": "object",
        "properties": {
          "location_type": {
            "type": "string",
            "description": "The general type of location where the show is set."
          },
          "specific_setting": {
            "type": "string",
            "description": "The specific setting within the location."
          }
        },
        "required": [
          "location_type",
          "specific_setting"
        ],
        "additionalProperties": false
      },
      "actress_information": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress."
          },
          "role_in_show": {
            "type": "string",
            "description": "Description of the actress's role in the identified show."
          },
          "known_for_film": {
            "type": "string",
            "description": "A film the actress is known for, as mentioned in the context or question."
          }
        },
        "required": [
          "name",
          "role_in_show",
          "known_for_film"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "show_name",
      "network",
      "show_type",
      "setting_details",
      "actress_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
