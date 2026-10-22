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
2017 AFL Goal of the Year: The Australian Football League celebrates the best goal of the season through the annual Goal of the Year competition.  In 2017, this is officially known as the Coates Hire AFL Goal of the Year.  Each round three goals are nominated and fans are able to vote online for their favourite at the league's website.  Daniel Rioli of Richmond was the winner with his banana goal kicked in round 3 against West Coast .  His selection as a finalist was controversial due to him not even winning the vote for Goal of the Week in round 3.

2014 AFL Goal of the Year: The Australian Football League celebrated the best goal of the season through the annual Goal of the Year competition.  In 2014, it was officially known as the Hungry Jacks AFL Goal of the Year.  Each round three goals were nominated and fans were able to vote online for their favourite at the league's website.

Goal of the Year (AFL): The Goal of the Year is a competition for the best goals kicked in the VFL/AFL during that season.  It is run in conjunction with the Mark of the Year competition and is currently sponsored by Coates Hire.  The award is also known as the Phil Manassa Medal.  The concept is thought to have been initiated as an unofficial award in 1970 by media interests after Alex Jesaulenko's famous mark.  The official award was first given in 2001.

2013 AFL Goal of the Year: The Australian Football League celebrates the best goal of the season through the annual Goal of the Year competition.  In 2013, this is officially known as the British Paints AFL Goal of the Year.  Each round three goals are nominated and fans are able to vote online for their favourite at the league's website.  At the end of the home and away season, three finalists were selected for a final public vote, which was won by Lance Franklin for his long-range goal after hurdling over a teammate in the middle of the ground.

2016 AFL Goal of the Year: The Australian Football League celebrates the best goal of the season through the annual Goal of the Year competition.  In 2016, this is officially known as the Coates Hire AFL Goal of the Year.  Each round three goals are nominated and fans are able to vote online for their favourite at the league's website.  Eddie Betts of the Adelaide Football Club was the winner with his goal kicked in round ten against the Greater Western Sydney Giants.

Premier League 20 Seasons Awards: The Premier League 20 Seasons Awards were a set of English football awards which marked the first 20 years of competition in the Premier League, the top-level domestic league competition of professional football in England.  The awards celebrated the first two decades of the Premier League, which was formed in 1992 when the 22 clubs of the old First Division resigned en-masse from The Football League.  Awards were presented in a number of categories for both teams and individuals, covering the period from the inaugural 1992–93 season which kicked off in August 1992, through to the 2011–12 season, which ended on 13 May 2012.  Voting ended on 30 April 2012.  Awards included best manager, best player and best goal.

2015 AFL Goal of the Year: The Australian Football League celebrates the best goal of the season through the annual Goal of the Year competition.  In 2015, this is officially known as the Coates Hire AFL Goal of the Year.  Each round three goals are nominated and fans are able to vote online for their favourite at the league's website.

Australian Football League reserves affiliations: The Australian Football League stages the highest-level senior Australian rules football competition in the country.  However, since the late 1980s, when the former Victorian Football League expanded interstate to become the modern Australian Football League, there has not been a league-wide reserves competition; and, since 2000, there has been no dedicated reserves competition of any kind.  As a result, AFL-listed players who are not selected in their senior teams are made eligible to play in one of the second-tier state leagues: the Victorian Football League, South Australian National Football League, West Australian Football League, or North East Australian Football League.  The system used to accommodate AFL-listed players within these leagues varies considerably from state to state.

2007 AFL Goal of the Year: The Australian Football League celebrates the best goal of the season through the annual AFL Goal of the Year competition.  In 2007, this is officially known as the Toyota AFL Mark of the Year

2011 AFL Goal of the Year: The Australian Football League celebrates the best goal of the season through the annual Goal of the Year competition.  In 2011, this is officially known as the Panasonic AFL Goal of the Year.  Each round three goals are nominated and fans are able to vote online for their favourite here .

Question: Who is the sponsor of the competition which celebrates the best goal of the season in the Australian Football League?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "competition_name": {
      "type": "string",
      "description": "The name of the competition."
    },
    "league_name": {
      "type": "string",
      "description": "The name of the sports league."
    },
    "sponsor_details": {
      "type": "object",
      "properties": {
        "sponsor_name": {
          "type": "string",
          "description": "The name of the sponsor."
        },
        "sponsorship_status": {
          "type": "string",
          "description": "Indicates if the sponsorship is current or past."
        }
      },
      "required": [
        "sponsor_name",
        "sponsorship_status"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "competition_name",
    "league_name",
    "sponsor_details"
  ],
  "additionalProperties": false
}
