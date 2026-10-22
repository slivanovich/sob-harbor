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
Franklin Field: Franklin Field is the home of the Penn Relays, and is the University of Pennsylvania's stadium for football, lacrosse and formerly for soccer, field hockey and baseball.  It is also used by Penn students for recreation, and for intramural and club sports, including touch football and cricket, and is the site of Penn's graduation exercises, weather permitting.

1996 NCAA Division I Field Hockey Championship: The 1996 NCAA Division I Field Hockey Championship was the 16th women's collegiate field hockey tournament organized by the National Collegiate Athletic Association, to determine the top college field hockey team in the United States.  The North Carolina Tar Heels won their third championship, defeating the Princeton Tigers in the final The championship rounds were held at the Boston College Field Hockey Field in Chestnut Hill, Massachusetts on the campus of Boston College.

2010 NCAA Division I Field Hockey Championship: The 2010 NCAA Division I Field Hockey Championship was the 30th women's collegiate field hockey tournament organized by the National Collegiate Athletic Association, to determine the top college field hockey team in the United States.  The Maryland Terrapins won its seventh championship, defeating the North Carolina Tar Heels in the final.  The semifinals and championship were hosted by the University of Maryland at the Maryland Field Hockey & Lacrosse Complex in College Park, Maryland.

2016 NCAA Division II Field Hockey Championship: The 2016 NCAA Division II Field Hockey Championship is the 28th women's collegiate field hockey tournament to determine the top NCAA Division II college field hockey team in the United States.  The semifinals and championship match will be played at W.B. Mason Stadium at Stonehill College in Easton, Massachusetts from November 18 to 20, 2016.

2009 NCAA Division I Field Hockey Championship: The 2009 NCAA Division I Field Hockey Championship was the 29th women's collegiate field hockey tournament organized by the National Collegiate Athletic Association, to determine the top college field hockey team in the United States.  The North Carolina Tar Heels field hockey won their sixth championship, defeating the Maryland Terrapins in the final.  The semifinals and championship were hosted by Wake Forest University at Kentner Stadium in Winston-Salem, North Carolina.

2014 NCAA Division I Field Hockey Championship: The 2014 NCAA Division I Field Hockey Championship is the 34th women's collegiate field hockey tournament organized by the National Collegiate Athletic Association, to determine the top college field hockey team from Division I in the United States.  The championship was played on November 23, 2014 at the Maryland Field Hockey & Lacrosse Complex, the home field of the host Maryland Terrapins, in College Park, Maryland.  The Connecticut Huskies won their fourth national championship, and second consecutive title, by defeating the Syracuse Orange, 1–0, in the final match.

2015 NCAA Division I Field Hockey Championship: The 2015 NCAA Division I Field Hockey Championship was the 35th women's collegiate field hockey tournament organized by the NCAA, to determine the top Division I college field hockey team in the United States.  The semifinals and championship match were played at the Ocker Field Hockey Field in Ann Arbor, Michigan from November 20 to 22, 2015.  This was the first time Michigan hosted the tournament finals.

1988 NCAA Division I Field Hockey Championship: The 1988 NCAA Division I Field Hockey Championship was the eighth women's collegiate field hockey tournament organized by the National Collegiate Athletic Association, to determine the top college field hockey team in the United States.  The Old Dominion Lady Monarchs won their fourth championship, defeating the Iowa Hawkeyes in the final.  The championship rounds were held at Franklin Field in Philadelphia, Pennsylvania.

2015 NCAA Division II Field Hockey Championship: The 2015 NCAA Division II Field Hockey Championship was the 27th women's collegiate field hockey tournament to determine the top NCAA Division II college field hockey team in the United States.  The semifinals and championship match were played at Steph Pettit Stadium at Bloomsburg University in Bloomsburg, Pennsylvania from November 20 to 22, 2015.

2007 NCAA Division I Field Hockey Championship: The 2007 NCAA Division I Field Hockey Championship was the 27th women's collegiate field hockey tournament organized by the National Collegiate Athletic Association, to determine the top college field hockey team in the United States.  The North Carolina Tar Heels won their fifth championship, defeating the Penn State Nittany Lions in the final.  The semifinals and championship were hosted by the University of Maryland at Maryland Field Hockey & Lacrosse Complex in College Park, Maryland.

Question: 1988 NCAA Division I Field Hockey Championship was held at what University's stadium?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "championship_year": {
      "type": "integer",
      "description": "The year the championship was held."
    },
    "championship_division": {
      "type": "string",
      "description": "The NCAA division of the championship."
    },
    "stadium_name": {
      "type": "string",
      "description": "The name of the stadium where the championship rounds were held."
    },
    "host_university": {
      "type": "string",
      "description": "The university that owns or is associated with the stadium."
    },
    "stadium_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the stadium is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the stadium is located."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "championship_year",
    "championship_division",
    "stadium_name",
    "host_university",
    "stadium_location"
  ],
  "additionalProperties": false
}
