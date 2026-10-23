{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKeaney Gymnasium: Keaney Gymnasium is a multi-purpose arena in Kingston, Rhode Island, United States.  The arena opened in 1953 and seats 3,385 (plus room for 500 standing-room only spectators).  It was home to the University of Rhode Island Rams men's and women's basketball teams before they moved to Ryan Center in 2002.  Since 2002, the volleyball team has called Keaney home.  The arena was named in honor of Rhode Island football coach, chemistry professor, basketball coach and athletic director Frank Keaney.  Seating is in a two-tiered arrangement, with the top tier being \"U\"-shaped.  At the west end of the arena there are bleachers in the former stage area of the building.  The arena hosted the NCAA Basketball Tournament first round games for three years, from 1967 to 1969.\n\nBolshoy Ice Dome: The Bolshoy Ice Dome (Russian: Большой Ледовый дворец ) is a multi-purpose indoor arena located in Olympic Park, Sochi, Russia.  Opened in 2012, the 12,000-seat arena was primarily constructed to host hockey competitions during the 2014 Winter Olympics.  Following the Games, it became the home arena of HC Sochi, an expansion team of the KHL.  The arena has also hosted concerts and other events.  Prior to the Games, the arena hosted the IIHF World U18 Championships and Channel One Cup in 2013.\n\nBarrie Arena: The Barrie Arena, sometimes also called the Dunlop Arena, was a 3,000 seat arena located in Barrie, Ontario, at the intersection of Dunlop Street West and Eccles Avenue.  It was built in 1932 and served as the main ice hockey venue in the city until the opening of the Barrie Molson Centre in 1995.  The arena hosted the Barrie Flyers of the Ontario Hockey League, and also briefly hosted the Barrie Colts while the BMC was under construction.\n\nMalmö Arena: Malmö Arena is a multi-use indoor arena in Malmö, Sweden, and the home of SHL ice hockey club Malmö Redhawks.  It is the largest arena in the SHL, and the second-largest indoor arena in Sweden.  Apart from hosting Redhawks hockey matches, the arena is often the venue for team handball, floorball, concerts, and other events.  It has also hosted indoor athletics.  Owned and operated by Parkfast AB, the arena was designed by Mats Matson of MM Matsson Konsult AB, Hannu Helkiö of Pöyry Architects, and Gert Wingårdh of Wingårdh arkitektkontor.  Naming rights for the venue are owned by Malmö Stad, in a ten-year contract, agreed in 2007.  Malmö Arena hosted the Eurovision Song Contest 2013 between 14 and 18 May 2013.\n\nSports Hall Diana: Diana Hall (Bulgarian: Зала \"Диана\" ) is a multifunctional Indoor arena in Yambol, Bulgaria.  The arena was opened in 1964 and has a seating capacity for 3,000 people .  It is the home of BC Yambol.  Besides basketball the arena is used for practicing trampolining, boxing, wrestling, shooting sport.  The arena hosted many national and European tournaments, such as the 2010 Bulgarian Basketball Cup, NBL all-star game 2015, Strandzha Cup, international wrestling tournament Dan Kolov.\n\nTD Garden: TD Garden, often called Boston Garden and \"The Garden\", is a multi-purpose arena in Boston, Massachusetts.  It is named after its sponsor, TD Bank, a subsidiary of Canada's Toronto-Dominion Bank.  It opened in 1995 as a replacement for the original Boston Garden and has been known as Shawmut Center, FleetCenter, and TD Banknorth Garden.  The arena is located directly above the MBTA's North Station.\n\nGinásio do Ibirapuera: Ginásio do Ibirapuera (officially named Ginásio Estadual Geraldo José de Almeida) is an indoor sporting arena located in São Paulo, Brazil.  The seating capacity of the arena is 11,000 people and it was opened on 25 January 1957.  Named after famous sports broadcaster and sports commentator Geraldo José de Almeida, in 2004, 2005 and 2006 Ginásio do Ibirapuera hosted the Salonpas Cup matches, and in 2006, the arena hosted the Basketball World Championship for Women.  Other notable basketball events include the 1973 Intercontinental Cup, the 1979 edition of the competition in which local E.C. Sírio won the title after a memorable win over Bosna Sarajevo, and the 1984 edition of the same competition in which Banco Roma won the title.\n\nSullivan Arena: The George M. Sullivan Arena (commonly shortened to the \"Sullivan Arena\" and often referred to colloquially as \"The Sully\") is a 6,290 seat arena in Anchorage, Alaska, United States.  It was home to the professional ice hockey team, the Alaska Aces of the ECHL and is currently home of the University of Alaska Anchorage Seawolves hockey team of the WCHA.  It is the former home of the Great Alaska Shootout basketball tournament which has relocated to the Alaska Airlines Center as of 2014, and is the current home of the Alaska Fighting Championship mixed martial arts events.  In 2007 it briefly became home to the Alaska Wild of the Indoor Football League which is now a defunct team.  The arena opened in 1983 and sits just east of Mulcahy Stadium as part of the Chester Creek Sports Complex.  Sullivan Arena hosted the 1989 World Junior Ice Hockey Championships along with the Harry J. McDonald Memorial Center in Eagle River.\n\nAlytus Arena: The Alytus Arena is a universal indoor arena in Alytus, Lithuania.  It was opened in 1977.  Its reconstruction began in 2009 and was completed by the end of 2010.  The arena was officially opened on 12 February 2011.  The arena hosted the Group C games of EuroBasket 2011 from 31 August 2011 to 5 September 2011.\n\nSummerSlam (2006): SummerSlam (2006) was the nineteenth annual SummerSlam professional wrestling pay-per-view (PPV) event produced by World Wrestling Entertainment (WWE).  It took place on August 20, 2006, at the TD Banknorth Garden in Boston, Massachusetts, and involved performers from the Raw, SmackDown! , and ECW brands.  This marked the first inter-brand pay-per-view including the ECW brand.\n\nQuestion: What arena hosted SummerSlam (2006) and opened in 1995\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"arena_name\": {\n      \"type\": \"string\",\n      \"description\": \"The official name of the arena.\"\n    },\n    \"opening_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the arena opened.\"\n    },\n    \"event_hosted\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the event hosted by the arena.\"\n    },\n    \"event_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the event took place.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the arena is located.\"\n    }\n  },\n  \"required\": [\n    \"arena_name\",\n    \"opening_year\",\n    \"event_hosted\",\n    \"event_year\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "arena_name": {
        "type": "string",
        "description": "The official name of the arena."
      },
      "opening_year": {
        "type": "integer",
        "description": "The year the arena opened."
      },
      "event_hosted": {
        "type": "string",
        "description": "The name of the event hosted by the arena."
      },
      "event_year": {
        "type": "integer",
        "description": "The year the event took place."
      },
      "location": {
        "type": "string",
        "description": "The city and state where the arena is located."
      }
    },
    "required": [
      "arena_name",
      "opening_year",
      "event_hosted",
      "event_year",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
