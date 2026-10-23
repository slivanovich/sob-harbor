{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEFL League Two: The English Football League Two (often referred to as League Two for short or Sky Bet League Two for sponsorship reasons) is the third-highest and lowest division of the English Football League (EFL) and fourth-highest division overall in the English football league system.\n\nIsle of Man Premier League: The Isle of Man Premier League (also known as the Canada Life Premier League for sponsorship reasons) is the highest division of the Isle of Man Football League and the highest overall in the Isle of Man football league system.  The Premier League, which was introduced for the 2007–08 season, was previously known as the First Division.  Each year, the top finishing club is crowned league champion, and the two lowest placed clubs are relegated to Division Two.\n\nList of Sunderland A.F.C. seasons: Sunderland Association Football Club was founded in 1879 as Sunderland & District Teachers Association Football Club by James Allan.  They turned professional in 1885.  Sunderland won their first Football League championship in the 1891–92 season two years after joining the league.  They won the next Football League First Division on three occasions in four seasons; in 1892, 1893 and 1895, separated by a runner-up spot in 1894.  In the 1901–02 season, Sunderland won their fifth Football League First Division championship.  They came close to completing the \"league and cup double\" in the 1912–13 season, winning the league but losing to Aston Villa in the 1913 FA Cup Final.  The team's next success came in the 1935–36 season when they won the League Championship and also the Charity Shield.  They had not won the FA Cup until the 1936–37 season when they defeated Preston North End in the 1937 FA Cup Final.  Sunderland entered The Football League in 1890 and were not relegated from the top division until the 1957–58 season; a total of 58 seasons in the highest division of England.  Their next trophy came in the 1973 FA Cup Final as they beat Leeds United 1–0.  They reached the 1985 Football League Cup Final but finished as runners-up to Norwich City after being beaten 1–0.  In the 1986–87 season Sunderland were relegated to the Football League Third Division for the first time in their history under the management of Lawrie McMenemy, they however, returned to the second division the following season as champions–their lowest position in the English football league system.  Their first appearance in the Premier League came in the 1999–2000 season after being promoted as champions from Division One.  In winning promotion the club gained 105 points, which was a record at the time.  Sunderland gained just 15 points in the 2005-06 season, which set the record for the lowest number of points in a Premier League season, which has since been eclipsed by Derby County.\n\nDiego De Girolamo: Diego Raymond De Girolamo (born 5 October 1995) is a professional footballer who plays as a forward for League Two club Chesterfield, on loan from Championship club Bristol City.\n\nChelsea F.C. league record by opponent: Chelsea Football Club is a professional association football club based Fulham, London.  Founded in 1905, they were elected to play in The Football League as members of the Second Division.  They were promoted into the First Division in the club's second season.  Chelsea remained in the Football League, in the First or Second division, until 1992 when clubs in the First Division broke away from The Football League to form the Premier League.  The club has remained in the top division of the English football league system since 1989.  In their latest spell in the Second Division Chelsea achieved their highest points total achieving 99 in the 1988–89 season.  As of the 2015–16 season, the club holds the records for the most points, most goals scored and most clean sheets in a single Premier League season with 95 points in 2004–05, 103 goals in 2009–10 and 25 clean sheets in 2004–05.  Chelsea have been English football champions six times.\n\nChesterfield F.C.: Chesterfield Football Club is a professional association football club based in the town of Chesterfield, Derbyshire, England.  The team competes in League Two, the fourth tier of the English football league system.  The club was a founding member of the Football League Third Division North in 1921–22 and has remained in the Football League since that time.  While they have never played in the top flight, they rose to the second tier twice in the 1930s.\n\nEFL Championship: The English Football League Championship (often referred to as the Championship for short or the Sky Bet Championship for sponsorship reasons) is the highest division of the English Football League and second-highest overall in the English football league system, after the Premier League.  Each year, the top finishing teams in the Championship are promoted to the Premier League, and the lowest finishing teams are relegated to League One.\n\nEFL Cup: The EFL Cup (referred to historically, and colloquially, as simply the League Cup), currently known as the Carabao Cup for sponsorship reasons, is an annual knockout football competition in men's domestic English football.  Organised by the English Football League (EFL), it is open to any club within the top four levels of the English football league system – 92 clubs in total – comprising the top level Premier League, and the three divisions of the English Football League's own league competition (Championship, League One and League Two).\n\nList of former English Football League clubs: The English Football League comprises professional football clubs from England and Wales.  It was established in 1888 as The Football League and in 1892 the Second Division was formed, with the existing division being renamed the First Division.  The First World War caused the League to be postponed from 1915 to 1919 and two seasons following its resumption a Third Division was introduced for one season, before being regionalised as North and South.  The 1958–59 season saw the introduction of a Fourth Division, with the top 12 clubs from the Third Division North and South from the previous season starting in a national Third Division, and the bottom 12 starting in the Fourth Division.  The introduction of the Premier League, which superseded the First Division as the top-flight of English football, caused a reorganisation of the English football league system in 1992, with the Fourth Division being disbanded.  The First Division, Second Division and Third Division were rebranded as the Championship, League One and League Two respectively ahead of the 2004–05 season, which came as part of a then-sponsorship with Coca-Cola.\n\nZak Jules: Zak Kennedy Jules (born 7 February 1997) is a Scottish professional footballer who plays for League Two club Chesterfield on loan from Shrewsbury Town, as a defender.\n\nQuestion: Diego Raymond De Girolamo, is a professional footballer who plays as a forward for League Two club Chesterfield, on loan from which organization, that's the highest division of the English Football League and second-highest overall in which football league system, after the Premier League?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_full_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the professional footballer.\"\n    },\n    \"current_club\": {\n      \"type\": \"string\",\n      \"description\": \"The club the player currently plays for.\"\n    },\n    \"loan_club\": {\n      \"type\": \"string\",\n      \"description\": \"The club the player is on loan from.\"\n    },\n    \"loan_club_division\": {\n      \"type\": \"string\",\n      \"description\": \"The division of the club the player is on loan from.\"\n    },\n    \"division_overall_rank\": {\n      \"type\": \"integer\",\n      \"description\": \"The overall rank of the division within its football league system (e.g., 1st, 2nd).\"\n    },\n    \"division_parent_league\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the parent league that the division belongs to.\"\n    },\n    \"football_league_system_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football league system to which the division belongs.\"\n    }\n  },\n  \"required\": [\n    \"player_full_name\",\n    \"current_club\",\n    \"loan_club\",\n    \"loan_club_division\",\n    \"division_overall_rank\",\n    \"division_parent_league\",\n    \"football_league_system_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_full_name": {
        "type": "string",
        "description": "The full name of the professional footballer."
      },
      "current_club": {
        "type": "string",
        "description": "The club the player currently plays for."
      },
      "loan_club": {
        "type": "string",
        "description": "The club the player is on loan from."
      },
      "loan_club_division": {
        "type": "string",
        "description": "The division of the club the player is on loan from."
      },
      "division_overall_rank": {
        "type": "integer",
        "description": "The overall rank of the division within its football league system (e.g., 1st, 2nd)."
      },
      "division_parent_league": {
        "type": "string",
        "description": "The name of the parent league that the division belongs to."
      },
      "football_league_system_name": {
        "type": "string",
        "description": "The name of the football league system to which the division belongs."
      }
    },
    "required": [
      "player_full_name",
      "current_club",
      "loan_club",
      "loan_club_division",
      "division_overall_rank",
      "division_parent_league",
      "football_league_system_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
