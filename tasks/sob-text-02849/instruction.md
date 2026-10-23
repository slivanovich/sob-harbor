{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNancy Carter: Nancy Carter is a fictional character from the BBC soap opera \"EastEnders\", played by Maddy Hill.  Nancy's first appearance is in a combination of the show's 4775th and 4776th episodes, originally broadcast in the United Kingdom on 1 January 2014.  A member of the Carter family, Nancy is the daughter of Mick Carter (Danny Dyer) and Linda Carter (Kellie Bright).  Her storylines include relationships with Wayne Ladlow (Malachi Kirby), Dexter Hartman (Khali Best) and Tamwar Masood (Himesh Patel), coping with the aftermath of her mother's rape, suffering from epilepsy and a feud with her older brother Lee Carter (Danny-Boy Hatchard).  On 12 March 2016, it was announced that Hill would be leaving the show, with Nancy making her final appearance alongside Tamwar on 22 April 2016.\n\nCris Carter: Graduel Christopher Darin \"Cris\" Carter (born November 25, 1965) is a former American football player in the National Football League.  He was a wide receiver for the Philadelphia Eagles (1987–89), the Minnesota Vikings (1990–2001) and the Miami Dolphins (2002).\n\nKenny Stafford: Kenny Stafford (born April 20, 1990) is a Canadian football wide receiver who is currently a member of the Edmonton Eskimos of the Canadian Football League (CFL).  In the United States he has been a member of the Atlanta Falcons (NFL), Pittsburgh Power (AFL) and Miami Dolphins (NFL).  Elsewhere in the CFL Stafford has been a member of the Calgary Stampeders, Montreal Alouettes and Winnipeg Blue Bombers.  He is the nephew of former American football wide receiver and 2013 Hall of Fame Inductee Cris Carter.\n\nList of NFL supplemental draft picks: There have been 43 players selected in the National Football League supplemental draft since its inception in 1977.  The supplemental draft was enacted in 1977 for players who had various circumstances affect their eligibility and did not enter the main NFL draft.  The only player selected in the supplemental draft to enter the Pro Football Hall of Fame was Cris Carter, who was selected in 1987 and elected to the Hall of Fame in 2013.  In addition, there have been eight players selected to Pro Bowls in their careers: Bernie Kosar (drafted in 1985), Cris Carter (1987), Bobby Humphrey (1989), Rob Moore (1990), Mike Wahle (1998), Jamal Williams (1998), Ahmad Brooks (2006), and Josh Gordon (2012).\n\n1999–2000 Toronto Raptors season: The 1999–2000 NBA season was the Raptors' fifth season in the National Basketball Association.  During the offseason, the Raptors acquired Antonio Davis from the Indiana Pacers, while signing free agents Muggsy Bogues and three-point specialist Dell Curry.  In their first full season playing at the Air Canada Centre, the Raptors got better as the season progressed.  Second-year star Vince Carter led the team in scoring, averaging 25.7 points per game.  He also won the Slam Dunk Contest in Oakland and was selected for the 2000 NBA All-Star Game.  The Raptors improved and qualified for their first playoff appearance with a 45–37 record, finishing third in the Central Division.  However, in the postseason, they were swept in the first round by the New York Knicks in three straight games.  Following the season, Tracy McGrady was traded to the Orlando Magic, Doug Christie was dealt to the Sacramento Kings, Dee Brown signed as a free agent with the Magic, and head coach Butch Carter was fired.\n\nButch Carter: Clarence Eugene \"Butch\" Carter (born June 11, 1958) is a retired American basketball player and coach.  He is the older brother of retired NFL wide receiver Cris Carter.\n\nDuron Carter: Duron Carter (born March 22, 1991) is a Canadian football wide receiver for the Saskatchewan Roughriders of the Canadian Football League (CFL).  Carter was a member of the Montreal Alouettes prior to signing with Saskatchewan on January 25, 2017 as a free agent.  He is the son of Pro Football Hall of Fame player Cris Carter, and played college football at Ohio State and Coffeyville Community College, but off-field issues and academic ineligibility prevented him continuing to play in Division I football.  He also attended Alabama and Florida Atlantic but did not play in a game for either school.  He entered the 2013 NFL Draft but was not selected.  Carter had a tryout for the Minnesota Vikings in 2013, but was not offered a contract.  He then played two years with the Alouettes before signing with the Indianapolis Colts of the National Football League (NFL).\n\nNick Carter (musician): Nickolas Gene \"Nick\" Carter (born January 28, 1980) is an American singer, songwriter, actor, and dancer.  He is best known as a member of the pop group the Backstreet Boys.  As of 2015, Carter has released three solo albums, \"Now or Never\", \"I'm Taking Off\" and \"All American\" during breaks between Backstreet Boys schedules, and a collaboration with Jordan Knight titled \"Nick & Knight\".  He has made occasional television appearances and starred in his own reality shows, \"House of Carters\" and \"I (Heart) Nick Carter\".  He gained fame in the mid 1990s and early 2000s as a teen idol.  He is also the older brother of singer Aaron Carter and the late Leslie Carter.\n\nCanadian Basketball League: The Canadian Basketball League (CBL) is a Canadian development league for men's basketball sports league.  The CBL was founded in July 2014 by former NBA coach Butch Carter.\n\nCarter Carburetor: Carter Carburetor Company in St. Louis, Missouri was established in 1909, and ceased operation in 1985.  It was founded by William Carter, who started experimenting with automotive carburetors while running a successful bicycle shop.  His first, cast brass carburetor could meter and deliver fuel more accurately than many competing units.  He sold Carter Carburetor Company 13 years after founding it to American Car and Foundry Company, a firm older than William Carter.  Carl Breer wrote that, upon learning that the Ball family (owners of Ball & Ball) was planning to leave the carburetor business, he set them up with Carter, which continued to produce the Ball & Ball basic designs used by Chrysler.\n\nQuestion: Who is older, Butch Carter or Cris Carter?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_older\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who is older.\"\n    },\n    \"person_younger\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who is younger.\"\n    },\n    \"older_person_birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the older person.\"\n    },\n    \"younger_person_birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the younger person.\"\n    },\n    \"age_comparison_result\": {\n      \"type\": \"string\",\n      \"description\": \"A statement indicating who is older based on their birth dates.\"\n    }\n  },\n  \"required\": [\n    \"person_older\",\n    \"person_younger\",\n    \"older_person_birth_date\",\n    \"younger_person_birth_date\",\n    \"age_comparison_result\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_older": {
        "type": "string",
        "description": "The name of the person who is older."
      },
      "person_younger": {
        "type": "string",
        "description": "The name of the person who is younger."
      },
      "older_person_birth_date": {
        "type": "string",
        "description": "The birth date of the older person."
      },
      "younger_person_birth_date": {
        "type": "string",
        "description": "The birth date of the younger person."
      },
      "age_comparison_result": {
        "type": "string",
        "description": "A statement indicating who is older based on their birth dates."
      }
    },
    "required": [
      "person_older",
      "person_younger",
      "older_person_birth_date",
      "younger_person_birth_date",
      "age_comparison_result"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
