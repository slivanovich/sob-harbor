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
Peter Tchernyshev: Peter Tchernyshev (Russian: Пётр Андреевич Чернышёв ; also romanized as "Pyotr Andreyevich Chernyshev"; born February 6, 1971) is a Russian-American ice dancer.  With skating partner Naomi Lang, he is a two-time (2000 and 2002) Four Continents champion, a five-time (1999–2003) U.S. national champion, and competed at the Winter Olympics in 2002.

Helga María Vilhjálmsdóttir: Helga María Vilhjálmsdóttir (born April 25, 1995 in Akureyri, Iceland) is an alpine skier from Iceland.  She will compete for Iceland at the 2014 Winter Olympics in the alpine skiing events.  She will become the first female athlete to represent the country at the Winter Olympics as well.

Anne Abernathy: Anne Abernathy (born April 12, 1953) is a luge athlete from the United States Virgin Islands and is the oldest female athlete to compete in the Winter Olympics.  The 2006 Winter Olympics were her sixth.  Despite her age, she is a strong competitor with numerous international podium finishes, and she is consistently ranked in the top 20 world rankings.  She is known within luge circles as "Grandma Luge."  She is training for the 2016 Summer Olympics as an archer.

Winter Olympic Games: The Olympic Winter Games (official name) (French: "Jeux olympiques d'hiver" ) is a major international sporting event held once every four years, for sports practised on snow and ice.  The first Winter Olympics, the 1924 Winter Olympics, was held in Chamonix, France.  The original five sports (broken into nine disciplines) were bobsleigh, curling, ice hockey, Nordic skiing (consisting of the disciplines military patrol, cross-country skiing, Nordic combined, and ski jumping), and skating (consisting of the disciplines figure skating and speed skating).  The Games were held every four years from 1924 to 1936, interrupted in 1940 and 1944 by World War II, and resumed in 1948.  Until 1992 the Winter and Summer Olympic Games were held in the same years, but in accordance with a 1986 decision by the International Olympic Committee (IOC) to place the Summer and Winter Games on separate four-year cycles in alternating even-numbered years, the next Winter Olympics after 1992 was in 1994.

Naomi Lang: Naomi Lang (born December 18, 1978) is an American ice dancer.  With skating partner Peter Tchernyshev, she is a two-time (2000 and 2002) Four Continents champion, a five-time (1999–2003) U.S. national champion, and competed at the 2002 Olympic Winter Games.  Lang is the first Native American female athlete to participate in the Winter Olympics.

Christopher Dean: Christopher Colin Dean, OBE (born 27 July 1958 in Calverton, Nottinghamshire) is an English ice dancer who won a gold medal at the 1984 Winter Olympics with his skating partner Jayne Torvill.  They also won a bronze medal at the 1994 Winter Olympics.

Suela Mëhilli: Suela Mëhilli (born January 28, 1994 in Vlorë, Albania) is an alpine skier from Albania.  She will compete for Albania at the 2014 Winter Olympics in the giant slalom competition.  She will become the first female athlete to represent the country at the Winter Olympics as well.

Ivana Bulatović: Ivana Bulatović (born October 12, 1994 in Berane, Montenegro) is an alpine skier from Montenegro.  She will compete for Montenegro at the 2014 Winter Olympics in the slalom competition.  She will become the first female athlete to represent the country at the Winter Olympics as well.

Australia at the 1952 Winter Olympics: Australia's second Winter Olympic Games appearance was at the 1952 Winter Olympics in Oslo, Norway.  It was 16 years since Australia's last Winter Games, as the 1940 and 1944 Winter Olympics were cancelled, and Australia did not compete in the 1948 Winter Olympics.  Australia sent nine athletes and competed in alpine skiing, cross-country skiing, figure skating and speed skating.  Nancy Hallam and Gweneth Molony were Australia's first women athletes at the Winter Olympics.

List of Olympic venues in figure skating: For the Summer and Winter Olympics, there are 27 venues that have been or will be used for figure skating.  This is one of two sports in the Winter Olympics to debut in the Summer Olympics with ice hockey being the other.  The first venue for the event took place during the 1908 Games was held indoors.  Twelve years later, the venue joined ice hockey as another Winter Olympic sport in the Summer Olympics.  For the first two Winter Olympics, figure skating was held outdoors.  With figure skating being held outdoors, there were weather concerns with thawing for the first two Winter Games.  A suggestion by International Olympic Committee President Count Henri de Baillet-Latour to 1932 Olympic Organizing Committee President Godfrey Dewey in September 1930 led Dewey to create the first indoor arena for the Winter Olympics.  For the 1936 Games, the venue was covered partially.  Following World War II, the 1948 venue became the first venue to be used twice at the Winter Olympics since it had been used twenty years earlier.  Figure skating's final competition that took place outdoors was in 1956 though that venue has since had a roof added to it.  Since 1960, all figure skating competitions have taken place indoors.  Three National Hockey League (NHL) venues have hosted Olympic figure skating competitions: the 1988 (both venues) and the 2010 though the NHL Vancouver Canucks moved out of the 2010 venue following the 1994–95 season.  The 2002 venue was a National Basketball Association (NBA) venue which meant the Utah Jazz was on a road trip during the 2002 Games.

Question: What year was the skating partner of the first Native American female athlete to participate in the Winter Olympics born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_native_american_female_athlete": {
      "type": "string",
      "description": "The name of the first Native American female athlete to participate in the Winter Olympics."
    },
    "skating_partner_name": {
      "type": "string",
      "description": "The name of the skating partner of the identified athlete."
    },
    "skating_partner_birth_year": {
      "type": "integer",
      "description": "The birth year of the skating partner."
    },
    "olympic_games_year": {
      "type": "integer",
      "description": "The year the athlete and partner competed in the Winter Olympics."
    }
  },
  "required": [
    "first_native_american_female_athlete",
    "skating_partner_name",
    "skating_partner_birth_year",
    "olympic_games_year"
  ],
  "additionalProperties": false
}
