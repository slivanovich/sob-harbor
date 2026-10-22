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
Maggie Shnayerson: Maggie Shnayerson (born Margot Beahan Shnayerson June 20, 1981 in New York, NY) is an American journalist and blogger.  She was an editor at Gawker Media's flagship site, Gawker.com and has written for "TIME" magazine, the "New York Sun", and the "New York Post".  Before joining Gawker, Shnayerson was the public relations director for the "Village Voice" and the "New York Sun".

Frank Isola (sportswriter): Frank Isola is an American sportswriter, who has been covering the New York Knicks and the National Basketball Association for the New York Daily News since 1996.  He also regularly appears on the ESPN show "Around the Horn" and SportsNet New York (SNY).  He is currently the lead host of "The Starting Lineup", which airs weekdays from 7-10am ET on SiriusXM NBA Radio.  Frank received an APSE sports writing award in 1998, and was voted New York Sportswriter of the Year in 2015.  New York Emmy Award in 2009-10.

Thom Loverro: Thomas F. Loverro (born March 25, 1954 in Brooklyn, New York), is an American sportswriter.  He was voted the Maryland sportswriter of the year in 2009 by the NSSA.

Henry Collins Brown: Henry Collins Brown (1862–1961) was a Scottish-born New York historian, lecturer, and author.  He was the founder of the Museum of the City of New York.  A Scottish immigrant, he arrived in New York at the age of 13.  After working as an advertising salesman, traveling throughout New York City, he became a journalist for "The New York Sun", writing about the city's history as well as its buildings.  Brown also wrote several books about New York's history, and was the editor of "Valentine's Manual".

History of the Brooklyn Dodgers: The Brooklyn Dodgers were an American baseball team that was active in the major leagues from 1884 until 1957, after which the club moved to Los Angeles, where it continued its history as the Los Angeles Dodgers.  The team's name derived from the reputed skill of Brooklyn residents at evading the city's trolley streetcar network.  The Dodgers played in two stadiums in South Brooklyn, each named Washington Park, and at Eastern Park in the neighborhood of Brownsville before moving to Ebbets Field in the neighborhood of Flatbush in 1913.  The team is noted for signing Jackie Robinson in 1947 as the first black player in the modern major leagues.

Frank Graham (writer): Frank Graham, Sr. (November 12, 1893 – March 9, 1965) was an American sportswriter and biographer.  He covered sports in New York for the "New York Sun" from 1915 to 1943 and for the "New York Journal-American" from 1945 to 1965.  He was also a successful author, writing biographies of politician Al Smith and athletes Lou Gehrig and John McGraw, as well as histories of the New York Yankees, New York Giants and Brooklyn Dodgers.  Graham's writing style was notable for his use of lengthy passages of "unrelieved dialogue" in developing portraits of the persons about whom he wrote.  Graham was posthumously inducted into the "writers wing" of the National Baseball Hall of Fame and Museum in 1972.  He was also posthumously honored in 1997 by the Boxing Writers Association of America with its highest honor, the A.J. Liebling Award.

Jack Newfield: Jack Abraham Newfield (February 18, 1938 – December 21, 2004) was an American muckraking journalist, columnist, author, documentary filmmaker, activist, and fierce champion of underdogs.  Newfield wrote for the "Village Voice", "New York Daily News", "New York Post", "New York Sun", "New York Magazine", "Parade Magazine", "Tikkun", "Mother Jones", and "The Nation" and monthly columns for several labor union newspapers.  Newfield believed that "the facts" should be contextualized within larger understandings.  In his autobiography, "Somebody's Gotta Tell It: The Upbeat Memoir of a Working-Class Journalist" (2002), Newfield stated, "The point is not to confuse objectivity with truth."  A career beat reporter, Newfield wrote prolifically about modern society, culture, and politics, on a range of topics relevant to urban life, such as municipal corruption, the police, and labor unions, and also professional sports, especially baseball and boxing, as well as contemporary music.  He authored numerous books about modern social and political subjects, including "A Prophetic Minority" (1966) and "Robert Kennedy : A Memoir."  His received the American Book Award for "The Full Rudy: The Man, the Myth, the Mania" about New York City Mayor Rudy Giuliani.  Newfield was a senior fellow at The Nation Institute, and an Emmy-award winning documentary filmmaker.

Pittsburgh Light Rail: The Pittsburgh Light Rail (commonly known as The T) is a 26.2 mi light rail system in Pittsburgh, Pennsylvania; it functions as a subway in Downtown Pittsburgh and largely as an at-grade light rail service in the suburbs south of the city.  The system is largely linear in a north-south direction, with one terminus just north of Pittsburgh's central business district and two termini in the South Hills.  The system is owned and operated by the Port Authority of Allegheny County.  It is the successor system to the streetcar network formerly operated by Pittsburgh Railways, the oldest portions of which date to 1903.  The Pittsburgh light rail lines are vestigial from the city's streetcar days, and is one of only three light rail systems in the United States that continues to use the Pennsylvania Trolley (broad) gauge rail on its lines instead of .  Pittsburgh is one of the few North American cities that have continued to operate light rail systems in an uninterrupted evolution from the first-generation streetcar era, along with Boston, Cleveland, New Orleans, Newark, Philadelphia, San Francisco and Toronto.

List of bus routes in Brooklyn: The Metropolitan Transportation Authority (MTA) operates a number of bus routes in Brooklyn, New York, United States; one minor route is privately operated under a city franchise.  Many of them are the direct descendants of streetcar lines (see list of streetcar lines in Brooklyn); the ones that started out as bus routes were almost all operated by the Brooklyn Bus Corporation, a subsidiary of the Brooklyn–Manhattan Transit Corporation, until the New York City Board of Transportation took over on June 5, 1940.  Of the 55 local Brooklyn routes operated by the New York City Transit Authority, roughly 35 are the direct descendants of one or more streetcar lines, and most of the others were introduced in full or in part as new bus routes by the 1930s.  Only the eastern section of the B82 (then the B50), the B83, and the B84 were created by New York City Transit from scratch, in 1978, 1966, and 2013, respectively.

Exhibition Boxing Bouts: Exhibition Boxing Bouts is the possible title for a very early American television series.  Aired 1931 to 1932 in New York City, it consisted of miniature boxing matches, and aired on what was then mechanical television station W2XAB, which later became WCBS-TV.  Time-slots varied from 15 minutes to 30 minutes, and it aired without commercials, as United States television was still an experimental service.  According to the section ""Radio Dial Log"" in the August 20, 1931 edition of "The New York Sun", one of the episodes featured a description by Harry Von Zell and Bill Schudt Jr, with Jimmie deForrest as the referee.  None of the episodes still exist, as it aired live, and practical methods to record live television did not exist until late 1947.  A still photograph of the series appears in page 19 of the February 20, 1932 edition of "The New York Sun", depicting two boxers in a small ring.

Question: What  team's name derived from the reputed skill of Brooklyn residents at evading the city's trolley streetcar network, who had a history wrote of it by an American sportswriter and biographer who  overed sports in New York for the "New York Sun" from 1915 to 1943?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_name": {
      "type": "string",
      "description": "The name of the sports team."
    },
    "name_origin_description": {
      "type": "string",
      "description": "The description of how the team's name originated."
    },
    "historian_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the sportswriter and biographer."
        },
        "occupation": {
          "type": "string",
          "description": "The primary occupation of the individual."
        },
        "covered_publication": {
          "type": "string",
          "description": "The publication for which the individual covered sports."
        },
        "coverage_start_year": {
          "type": "integer",
          "description": "The start year of their coverage for the specified publication."
        },
        "coverage_end_year": {
          "type": "integer",
          "description": "The end year of their coverage for the specified publication."
        },
        "wrote_team_history": {
          "type": "boolean",
          "description": "Indicates if this historian wrote a history of the specified team."
        },
        "other_historical_subjects": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other subjects or teams for which the historian wrote histories or biographies."
        }
      },
      "required": [
        "name",
        "occupation",
        "covered_publication",
        "coverage_start_year",
        "coverage_end_year",
        "wrote_team_history",
        "other_historical_subjects"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "team_name",
    "name_origin_description",
    "historian_details"
  ],
  "additionalProperties": false
}
