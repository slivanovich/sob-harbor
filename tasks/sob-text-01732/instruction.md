{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAnne, Princess Royal: Anne, Princess Royal, {'1': \", '2': \", '3': \", '4': \"} (Anne Elizabeth Alice Louise; born 15 August 1950) is the second child and only daughter of Queen Elizabeth II and Prince Philip, Duke of Edinburgh.  At the time of her birth, she was third in the line of succession to the British throne, behind her mother – then Princess Elizabeth – and elder brother, Charles.  She rose to second after her mother's accession, but is currently 12th in line.\n\nPeter Phillips: Peter Mark Andrew Phillips (born 15 November 1977) is the elder child and only son of Anne, Princess Royal, and her first husband, Captain Mark Phillips.  He is the eldest grandchild of Queen Elizabeth II and Prince Philip, Duke of Edinburgh.  After graduating from university in 2000, he worked for Jaguar followed by WilliamsF1.  In 2003, while working for WilliamsF1 in Canada, he met Autumn Kelly, whom he married in St George's Chapel at Windsor Castle in 2008.  For many years Phillips has worked in the sports sponsorship and management fields.  He is currently 13th in line of succession to the British throne.\n\nAndrew Phillips (swimmer): Andrew Phillips (born 17 April 1962) is a Jamaican swimmer.  He competed in four events at the 1984 Summer Olympics.\n\nAfter School Massacre: After School Massacre (originally titled Teacher's Day) is a 2014 American slasher film written and directed by Jared Masters.  The film stars Nikole Howell, Lindsay Lamb, Andrew Phillips, Courtney Rood, Danika Galindo, Yasmine Soofi, and Savannah Matlow.  \"After School Massacre\" follows the story of a high school teacher who goes on a killing spree after being fired, stalking his former female students at their slumber party.\n\nWendy Phillips (author): Wendy Philips is a Canadian author.  She grew up in Kamloops, British Columbia, and wrote her first book at the age of 11, and completed degrees in Journalism, English, Education and a Children’s Literature degree from the University of British Columbia in Vancouver, BC.  Her past jobs have included journalism, bookbinding and teaching English.  She has lived in Lesotho, Ottawa, South Africa and Australia, but currently lives in Richmond, British Columbia with her husband, son and daughter.  Phillips currently works as a teacher-librarian at MacNeill Secondary School in Richmond, BC.  Phillips is also an author of young adult fiction, whose first book \"Fishtailing\" won the 2010 Governor General’s Award for children’s literature.\n\nGrasscut: Grasscut are composer/producer Andrew Phillips and musician/writer Marcus O’Dair.  Phillips writes and produces all Grasscut music; he also sings and plays various instruments including guitar and keyboards.  O'Dair manages the act and contributes keyboards and double bass.  They are based in Brighton, England.\n\nSteve Phillips (Political Leader): Steve Phillips is a New York Times bestselling author, national liberal political leader, civil rights lawyer, and a senior fellow at the Center for American Progress.  Phillips is founder and chairman of PowerPac+.  He is also founder of PowerPAC.org.  Phillips currently splits his time between San Francisco and Washington, D.C.\n\nAndrew Phillips (lawyer): Andrew Phillips is a deaf lawyer, and an advocate for equal access.\n\nJohn Phillips (musician): John Edmund Andrew Phillips (August 30, 1935 – March 18, 2001) was an American singer, guitarist, songwriter, and promoter, most notably of the 1967 Monterey Pop Festival, a landmark event of the counterculture era and the Summer of Love.  Known as Papa John, Phillips was a member and leader of the vocal group The Mamas & the Papas.\n\nAndrew Phillips (footballer, born 1970): Andrew Phillips (born 27 January 1970) is a former Australian rules footballer who played with Carlton in the Australian Football League (AFL).\n\nQuestion: Where in the line of accession is the mother of Peter Mark Andrew Phillips currently?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person whose line of succession is being queried.\"\n    },\n    \"relationship_to_peter_phillips\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the person to Peter Phillips.\"\n    },\n    \"current_line_of_succession\": {\n      \"type\": \"string\",\n      \"description\": \"The current position in the line of succession to the British throne.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"relationship_to_peter_phillips\",\n    \"current_line_of_succession\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person whose line of succession is being queried."
      },
      "relationship_to_peter_phillips": {
        "type": "string",
        "description": "The relationship of the person to Peter Phillips."
      },
      "current_line_of_succession": {
        "type": "string",
        "description": "The current position in the line of succession to the British throne."
      }
    },
    "required": [
      "person_name",
      "relationship_to_peter_phillips",
      "current_line_of_succession"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
