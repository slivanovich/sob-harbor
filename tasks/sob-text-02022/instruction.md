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
Charlene Holt: Verna Charlene Stavely, professionally known as Charlene Holt, was an American actress known for her supporting roles in television and film.

Apache Drums: Apache Drums is a 1951 American Technicolor Western film directed by Hugo Fregonese and produced by Val Lewton.  The drama features Stephen McNally, Coleen Gray, and Willard Parker.  The film was based on an original story: "Stand at Spanish Boot", by Harry Brown.  "Apache Drums" was the last film Val Lewton produced before his death.

Harry Brown (film): Harry Brown is a 2009 British vigilante action-thriller film directed by Daniel Barber and starring Sir Michael Caine, Emily Mortimer, Jack O'Connell, and Liam Cunningham.  The story follows Harry Brown, a widowed Royal Marines veteran who had served in Northern Ireland during The Troubles, living on a London housing estate that is rapidly descending into youth crime.  After a violent gang murders his friend, Harry decides to take justice into his own hands.

Smoky (1966 film): Smoky is a 1966 Western film, directed by George Sherman.  It stars Fess Parker, Diana Hyland, Katy Jurado and Hoyt Axton.  The third of three film adaptations of the 1926 children's novel "Smoky the Cowhorse" by Will James, it utilizes the screenplay from the 1946 film.

El Dorado (1966 film): El Dorado is a 1966 American Western film produced and directed by Howard Hawks and starring John Wayne and Robert Mitchum.  Written by Leigh Brackett and loosely based on the novel "The Stars in Their Courses" by Harry Brown, the film is about a gunfighter who comes to the aid of an old friend—a drunken sheriff struggling to defend a rancher and his family against another rancher trying to steal their water.  The gunfighter and drunken sheriff are helped by an aging Indian fighter and a young gambler.  The supporting cast features James Caan as the young gambler, Charlene Holt, Ed Asner, Paul Fix, Arthur Hunnicutt, Michele Carey, and Christopher George.

Texas Across the River: Texas Across The River is a 1966 western film comedy/satire with Dean Martin, Alain Delon, Rosemary Forsyth and Joey Bishop.  The film was directed by Michael Gordon.

Only the Valiant: Only the Valiant, also known as Fort Invincible, is a 1951 Western film produced by William Cagney (younger brother of James Cagney), directed by Gordon Douglas starring Gregory Peck, Barbara Payton, Ward Bond.  The screenplay was written by Edmund H. North and Harry Brown, based on the 1943 novel of the same name by Charles Marquis Warren.

Duel at Diablo: Duel at Diablo is a 1966 western film starring James Garner in his first Western since leaving "Maverick" and Sidney Poitier in his first Western.  Based on Marvin H. Albert's 1957 novel "Apache Rising", the film was written by Albert and Michael M. Grilikhes and directed by Ralph Nelson who had directed Poitier in "Lilies of the Field".  The supporting cast includes Bibi Andersson, Bill Travers, Dennis Weaver and John Hoyt; Ralph Nelson has a cameo as an Army Major.  The movie was shot on location amidst striking scenery in Utah; the musical score was composed by Neal Hefti.

Savage Pampas (1966 film): Savage Pampas is a 1966 western film directed by Hugo Fregonese and starring Robert Taylor, Ron Randell and Marc Lawrence.  The film was a co-production between Argentina, Spain and the United States, and was a remake of the 1945 Argentine film of the same title which Fregonese had co-directed.  The film's location shooting took place in Spain, a popular location for westerns during the era.  The film's action is set in the Argentinian Pampas around the time of the Conquest of the Desert.

Paul Fix: Peter Paul Fix (March 13, 1901 – October 14, 1983) was an American film and television character actor, best known for his work in Westerns.  Fix appeared in more than a hundred movies and dozens of television shows over a 56-year career spanning from 1925 to 1981.  Fix was best known for portraying Marshal Micah Torrance, opposite Chuck Connors's character in "The Rifleman" from 1958–1963.  Fix later appeared with Chuck Connors in the 1966 western film "Ride Beyond Vengeance".

Question: Charlene Hollt played in a 1966 western film based on what Harry Brown novel

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film Charlene Holt appeared in."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "actress_name": {
      "type": "string",
      "description": "The name of the actress in the film."
    },
    "author_name": {
      "type": "string",
      "description": "The name of the author whose novel the film was based on."
    },
    "novel_title": {
      "type": "string",
      "description": "The title of the Harry Brown novel the film was based on."
    }
  },
  "required": [
    "film_title",
    "film_year",
    "film_genre",
    "actress_name",
    "author_name",
    "novel_title"
  ],
  "additionalProperties": false
}
