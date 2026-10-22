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
Canada men's national inline hockey team: The Canadian men's national inline hockey team is the national team for Canada, based in Dauphin, Manitoba (NIHA) and Richmond Hill, Ontario (Inline Canada).  The team is controlled by the National Inline Hockey Association - Canada for IIHF events and Inline Canada for FIRS events.

Great Britain women's national inline hockey team: Great Britain women's national inline hockey team is the national team for Great Britain.  The team finished sixth at the 2011 Women's World Inline Hockey Championships.  The team competed in the 2013 Women's World Inline Hockey Championships.

Sweden men's national inline hockey team: The Swedish men's national inline hockey team is one of the most successful inline hockey teams in the world.  With notable alumni like Henrik Lundqvist the Swedes have won five gold medals as members of the Top Division at the IIHF Inline Hockey World Championships.

Czech Republic men's national inline hockey team: The Czech men's national inline hockey team is the national team for the Czech Republic.  The Czechs have won two medals at the IIHF Inline Hockey World Championships, despite the fact that NHL players have frequently been on the team roster.  Most recently, the team finished seventh at the 2007 Men's World Inline Hockey Championships.

Finland men's national inline hockey team: The Finnish men's national inline hockey team is the national team for Finland.  Finland has been one of the most successful teams at the IIHF Inline Hockey World Championships which were organized annually from 1996 until 2015 with the exception of the year 1999.  Starting from 2017, the tournament will be held every other year.  Finland has won a total of thirteen medals in nineteen tournaments.  Most recently, the team finished in 2nd place in the 2015 Men's World Inline Hockey Championships in Tampere, Finland.

Germany women's national inline hockey team: Germany women's national inline hockey team is the national team for Germany.  The team finished eighth at the 2011 Women's World Inline Hockey Championships.  The team competed in the 2013 Women's World Inline Hockey Championships.

Australia men's national inline hockey team: The Australia men's national inline hockey team represents Australia in international inline hockey competitions.  They are controlled by Ice Hockey Australia for events organised by the International Ice Hockey Federation and by Skate Australia for events organised by the International Roller Sports Federation.  Australia plays in Division I of the IIHF InLine Hockey World Championship and Group C at the FIRS Inline Hockey World Championships.

United States men's national inline hockey team: The United States men's national inline hockey team is based in Colorado Springs, Colorado.  The team that competes in the IIHF InLine Hockey World Championships is controlled by USA Hockey, while the team that competes in the FIRS Senior Men's Inline Hockey World Championships is controlled by USA Roller Sports.  The United States has won 6 of 18 IIHF gold medals and 14 of 18 FIRS gold medals at world championships.

Chile national inline hockey team: The Chilean national inline hockey team represents inline hockey in Chile at international competitions.  The team have not played any world championship until the National Association of Hockey on Ice and Inline was founded and it joined the IIHF in 2000.  The team does however participate in the IIHF Inline Hockey World Championship and FIRS Inline Hockey World Championships (organised by International Roller Sports Federation).  Chile has rinks in Santiago and Puerto Montt, where ice hockey is being developed.

Henrik Lundqvist: Henrik Lundqvist (] ; born 2 March 1982) is a professional ice hockey goaltender for the New York Rangers of the National Hockey League (NHL).  Before winning the Vezina Trophy in 2012, he was nominated in each of his first three seasons, and is the only goaltender in NHL history to record ten 30 win seasons in his first 11 seasons.  He currently holds the record for most wins by a European-born goaltender in the NHL (405 as of August 13, 2017).  His dominating play during his rookie season resulted in the New York media and Rangers fans giving him the nickname "King Henrik".  During the 2006 Winter Olympics in Turin, Italy, he led the Swedish men's team to their second Olympic gold medal.

Question: Which National Hockey League (NHL) team did the man, who is a notable alumnus of the Sweden men's national inline hockey team, play for?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual who is a notable alumnus."
    },
    "alumnus_of_team": {
      "type": "string",
      "description": "The national inline hockey team the person is an alumnus of."
    },
    "nhl_team": {
      "type": "string",
      "description": "The National Hockey League (NHL) team the person played for."
    },
    "nhl_team_location": {
      "type": "string",
      "description": "The city where the NHL team is based."
    }
  },
  "required": [
    "person_name",
    "alumnus_of_team",
    "nhl_team",
    "nhl_team_location"
  ],
  "additionalProperties": false
}
