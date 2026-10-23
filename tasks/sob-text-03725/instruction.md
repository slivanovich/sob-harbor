{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRod Strickland: Rodney Strickland (born July 11, 1966) is an American retired National Basketball Association (NBA) player.  Strickland played college basketball at DePaul University, where he was awarded All-American honors.  He then enjoyed a long career in the NBA, playing from 1988 to 2005.  Strickland is currently an assistant coach for the South Florida Bulls, under Orlando Antigua.  He formerly served in an administrative role for the University of Kentucky basketball team under head coach John Calipari and was the director of basketball operations at the University of Memphis under Calipari.  He is the godfather of current NBA player Kyrie Irving.\n\nNBA Live 14: NBA Live 14 is a basketball video game released on the PlayStation 4 and Xbox One in 2013.  \"NBA Live 14\" features Kyrie Irving of the Cleveland Cavaliers as its cover athlete.  It is one of the most negatively received games in its franchise.  \"NBA Live 14\" was followed by \"NBA Live 15\" which was released in October 2014.  The game marks the first installment in the series since \"NBA Live 10\".\n\nBig Three (Cleveland Cavaliers): The Big Three were a trio of professional basketball players for the Cleveland Cavaliers of the National Basketball Association (NBA) that played together from the 2014–15 NBA season to the 2016-17 NBA season .  The Big Three consisted of NBA all-stars point guard Kyrie Irving, small forward LeBron James, and power forward Kevin Love.  All three players were selected within the first five picks of their respective drafts, with Irving and James going number one overall, prior to the trio's formation.\n\nKyrie Irving: Kyrie Andrew Irving ( , born March 23, 1992) is an American professional basketball player for the Boston Celtics of the National Basketball Association (NBA).  He was named NBA Rookie of the Year after being selected by the Cleveland Cavaliers with the first overall pick in the 2011 NBA draft.  A four-time NBA All-Star, Irving was selected to the All-NBA Third Team in 2015.  He won an NBA Championship with the Cavaliers in 2016.\n\n2014–15 Cleveland Cavaliers season: The 2014–15 Cleveland Cavaliers season was the 45th season of the franchise in the National Basketball Association (NBA).  The season was marked by the publicity the team received by signing free agent forward LeBron James and trading for forward Kevin Love.  These All-Star players, added with All-Star guard Kyrie Irving, were dubbed nationally as the \"Big Three\".  A sub-.500 team the previous four seasons, the Cavaliers won the Central division with a 53–29 record.  Despite losing key players to injuries, their run continued until deep in the NBA Playoffs, eventually making it to the NBA Finals, their second appearance since 2007.  The Cavaliers' season ended with a 2–4 series loss to the Golden State Warriors in the NBA Finals.\n\nNBA 2K18: NBA 2K18 is a basketball simulation video game developed by Visual Concepts and published by 2K Sports.  It is the 19th installment in the \"NBA 2K\" franchise and the successor to \"NBA 2K17\".  It was released in September 2017 for Microsoft Windows, Nintendo Switch, PlayStation 4, PlayStation 3, Xbox One, and Xbox 360.  Kyrie Irving serves as cover athlete for the regular edition of the game, Shaquille O'Neal is the cover athlete for the special editions, and DeMar DeRozan of the Toronto Raptors is the cover athlete for the game in Canada.  While a member of the Cleveland Cavaliers when selected for the cover, Irving was traded to the Boston Celtics prior to the game's release.  As a result, a new cover depicting Irving in a Celtics uniform was revealed alongside the original cover.\n\n2010–11 Duke Blue Devils men's basketball team: The 2010–11 Duke Blue Devils men's basketball team represented Duke University in the 2010–11 NCAA Division I men's basketball season.  Returning as head coach was Hall of Famer Mike Krzyzewski.  The team played its home games at Cameron Indoor Stadium in Durham, North Carolina and are members of the Atlantic Coast Conference.  The team finished the regular season with a record of 30–4, ranked #1 in the media polls a total of eleven weeks during the season.  They also won the ACC Tournament, winning for the third consecutive year.  As the #1 seed in the west region of the 2011 NCAA Men's Division I Basketball Tournament, they defeated Hampton in the second round and Michigan in the third round to advance to the \"Sweet Sixteen\" where they were defeated by Arizona to finish the season 32–5.  Their best player Kyrie Irving played an important role on their team.  Kyrie Irving's backup was Karl Colombus.\n\nBen Simmons: Benjamin David Simmons (born 20 July 1996) is an Australian professional basketball player for the Philadelphia 76ers of the National Basketball Association (NBA).  A versatile forward from Melbourne, Simmons attended Box Hill Senior Secondary College before moving to the United States to attend Montverde Academy in Montverde, Florida.  He played one season of college basketball for Louisiana State University (LSU), where he was named a consensus first-team All-American and the USBWA National Freshman of the Year.  Simmons was selected with the number one overall pick in the 2016 NBA draft by the 76ers, becoming the third Melbourne-born number one overall pick (following Andrew Bogut and Kyrie Irving) in 11 years.  He has also represented the Australian national team.\n\nEntertainer's Basketball Classic: Entertainer's Basketball Classic is a basketball tournament held at Rucker Park in New York City.  In 1986, the original Rucker Park Tournament became the Entertainers Basketball Classic.  Participants of the tournament include NBA professionals and NCAA elite players including Allen Iverson, Stephon Marbury, Wilt Chamberlain, Kobe Bryant, Julius Erving, Kyrie Irving, from schools like Syracuse University\n\n2017–18 Boston Celtics season: The 2017–18 Boston Celtics season will be the 72nd season of the franchise in the National Basketball Association (NBA).  They originally acquired the #1 pick of the NBA draft due to a previous trade involving the Brooklyn Nets, only to then trade the #1 pick of the NBA draft to the Philidelphia 76ers in exchange for two different draft picks.  They also acquired Gordon Hayward in free agency on July 7 and Kyrie Irving via trade on August 22, 2017 in exchange for rookie Ante Žižić, Jae Crowder, star point guard Isaiah Thomas, the Brooklyn Nets' completely unprotected first round pick in the 2018 NBA draft, and later adding a 2020 second round pick originally from the Miami Heat eight days later.  The Celtics will play the first game of the regular season on October 17, 2017 against the Cleveland Cavaliers, Irving's former team, and retire the number 34 of former small forward Paul Pierce on February 11, 2018 against the Cavs.\n\nQuestion: Rod Strickland and Kyrie Irving, are Americans that have which organization in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person mentioned.\"\n    },\n    \"person_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person mentioned.\"\n    },\n    \"shared_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality shared by both individuals.\"\n    },\n    \"common_organization\": {\n      \"type\": \"string\",\n      \"description\": \"The organization that both individuals have in common.\"\n    },\n    \"organization_acronym\": {\n      \"type\": \"string\",\n      \"description\": \"The acronym for the common organization, if available.\"\n    },\n    \"person_1_status_in_organization\": {\n      \"type\": \"string\",\n      \"description\": \"Rod Strickland's status or role related to the common organization.\"\n    },\n    \"person_2_status_in_organization\": {\n      \"type\": \"string\",\n      \"description\": \"Kyrie Irving's status or role related to the common organization.\"\n    }\n  },\n  \"required\": [\n    \"person_1_name\",\n    \"person_2_name\",\n    \"shared_nationality\",\n    \"common_organization\",\n    \"organization_acronym\",\n    \"person_1_status_in_organization\",\n    \"person_2_status_in_organization\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1_name": {
        "type": "string",
        "description": "The name of the first person mentioned."
      },
      "person_2_name": {
        "type": "string",
        "description": "The name of the second person mentioned."
      },
      "shared_nationality": {
        "type": "string",
        "description": "The nationality shared by both individuals."
      },
      "common_organization": {
        "type": "string",
        "description": "The organization that both individuals have in common."
      },
      "organization_acronym": {
        "type": "string",
        "description": "The acronym for the common organization, if available."
      },
      "person_1_status_in_organization": {
        "type": "string",
        "description": "Rod Strickland's status or role related to the common organization."
      },
      "person_2_status_in_organization": {
        "type": "string",
        "description": "Kyrie Irving's status or role related to the common organization."
      }
    },
    "required": [
      "person_1_name",
      "person_2_name",
      "shared_nationality",
      "common_organization",
      "organization_acronym",
      "person_1_status_in_organization",
      "person_2_status_in_organization"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
