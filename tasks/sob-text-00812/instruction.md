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
Croxley Green: Croxley Green is a large suburb of Rickmansworth and a civil parish in England with a population recorded at the 2011 Census of 12,562.

Barry A. Vann: Barry Aron Vann (born 1960) is an author, speaker and Chair of the Institute for Leadership Studies and professor of geography at University of the Cumberlands.  A prolific writer, Vann has published on a wide range of geographic topics.  He is most noted for his work in environmental perceptions and religious geography, in particular themes in which religious beliefs are associated with forming environmental perceptions and politicized regions such as Northern Ireland and the American Bible Belt.  Vann's work along the interface between religion and geography stresses the role of faith leaders in shaping the behaviors of others who in turn impact the cultural landscape.  An excellent description of how Vann conjoins geotheology and leadership, or the lack thereof, is expressed by Andrew Nicholls in The Journal of British Studies: “Vann acknowledges that the early Stuart policy of plantation facilitated the emigration of Scots to Ireland, and for those who feared and loathed the religious policies of the regime, early seventeenth century Ulster [nine northern counties in Ireland] could stand as a land of refuge.  But only for some.  Scotland featured numerous socioeconomic challenges, and for some dissenters, rising rents, unproductive lands, and failed crops were evidence of punishment from an angry God.  Therefore, migration became an opportunity to atone for one’s sins as well, although individuals leaving Scotland owing to poverty could expect little sympathy from their religious leaders.”  His book "Puritan Islam: The Geoexpansion of the Muslim World" was chosen as a Top 25 Outstanding Academic Title for 2012 by "Choice", a division of the American Library Association (ALA).  A review in the April 2012 issue of "Choice" referred to "Puritan Islam" as "perhaps the best geographical text produced on this subject since 2000" and of "utmost significance in finally taking the topic away from the emotional to where it needs to be--rational and explanatory discussion."  On her show "Spirited Debate", Lauren Green of Fox News called "Puritan Islam" a "fascinating book."

Richard Woitach: Richard Woitach (born 1936) is an American conductor, pianist, and composer.  In 1959, after studying music at the Eastman School of Music, Woitach jointed the Metropolitan Opera in New York City and served as a staff conductor there until 1997.  In 1981, he collaborated with Canadian operatic soprano Teresa Stratas to record "The Unknown Kurt Weill", a landmark Nonesuch record that introduced unpublished songs of German composer Kurt Weill and for which Woitach received a Grammy nomination in 1982.  Woitach also was a long time collaborator with Canadian heldentenor Jon Vickers, where Woitach accompanied Vickers on the piano in several recorded recitals in both Canada and New York City.  Woitach lives with his wife soprano Jeryl Metz in the Upper West Side of New York City.

Debra!: Debra!  (originally Decidedly Debra!)  is a Canadian television series that focuses on 14-year-old Debra Delong, who wants to make her own company and wants to run it with a boy named Preston Lunford.  The series was created by Andrew Nicholls, and Darrell Vickers, and produced by Cookie Jar Group.  "Debra!"  is executive-produced by Stacey Stewart Curtis, and produced by Kevin May.  The series was cancelled on January 1, 2012.

Andrew Nicholls and Darrell Vickers: Andrew Nicholls (born 14 July 1957, in Croxley Green, England) and Darrell Vickers (born 17 July 1957, in England) are a prolific Hollywood writing team.  Though both their families moved independently from England to the same town in Canada, Nicholls and Vickers didn't meet until junior high in 1969, where they began collaborating almost immediately.  The writing duo moved to Los Angeles in 1983 to continue their careers, and are members of WGA, WGC, SACD, SOCAN, ACCT, and ATAS.

Nicholls, Georgia: Nicholls is a city in Coffee County, Georgia, United States.  The population was 2,798 as of the 2010 census, up from 1,008 in 2000, due to counting of the Coffee County Correctional Facility population within the city limits.  This facility is privately owned and operated by CoreCivic.

David Shaw Nicholls: David Shaw Nicholls (born 27 February 1959 in Bellshill, Scotland) is a Scottish architect and designer based in New York City.  Nicholls is known for his work on furniture, modern area rug and textile designs.  Nicholls studied art, architecture and design at Edinburgh College of Art (Edinburgh, Scotland) and Domus Academy (Milan, Italy), before starting his own product and textile design firm in New York City.

Drexell's Class: Drexell's Class is an American sitcom that aired Thursday at 8:30 on Fox as part of its 1991-92 lineup.  The show was created by Andrew Nicholls and Darrell Vickers.

Blind (band): Blind was a Christian rock band formed in Wollongong, Australia in 1999 and consisted of Greg Bell (guitar), Adrian Deck (drums/vocals), Andrew Nicholls (vocals 2001–2005), Michael Molkentin (bass) and Chris Stewart (vocals 1999–2000).

Andrew Vickers: Andrew Julian Vickers (born 1967) is a biostatistician and attending research methodologist at Memorial Sloan Kettering Cancer Center.  Since 2013, he has also been professor of public health at Weill Cornell Medical College.  He is the statistical editor for the peer-reviewed journal "European Urology".

Question: What was the population of the city where Andrew Nicholls and Darrell Vickers was born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "birth_city_name": {
      "type": "string",
      "description": "The name of the city where Andrew Nicholls was born."
    },
    "birth_city_country": {
      "type": "string",
      "description": "The country where the birth city is located."
    },
    "population_count": {
      "type": "integer",
      "description": "The population of the city."
    },
    "population_census_year": {
      "type": "integer",
      "description": "The year the population was recorded."
    },
    "individuals_born_there": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of individuals mentioned in the context who were born in this city."
    }
  },
  "required": [
    "birth_city_name",
    "birth_city_country",
    "population_count",
    "population_census_year",
    "individuals_born_there"
  ],
  "additionalProperties": false
}
