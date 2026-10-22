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
John Mullaly: John Mullaly (1835–1915), known as father of the Bronx's park system, was a newspaper reporter and editor who was instrumental in forming the New York Park Association.  He was born in Belfast, Ireland.  After coming to the United States, he worked for the New York Herald, the New York Tribune, and the New York Evening Post.  He was the editor of the Metropolitan Record, published by the Catholic Church in New York City.

William Coleman (editor): William Coleman (February 14, 1766 – July 13, 1829) was the first editor of "The New York Evening Post" (today known as the "New York Post"), chosen by founder Alexander Hamilton.

John Charles Martin: John Charles Martin was an American newspaper publisher.  Beginning in 1913, ran the newspapers purchased by his step father-in-law Cyrus Curtis, including the "Public Ledger", the "New York Evening Post", the "Philadelphia Inquirer" and four others.  In 1931, an insurance industry magazine published a listing of Americans carrying the greatest amount of life insurance; Martin was second on the list with $6,540,000 in insurance, after Pierre Samuel du Pont with $7 million.

Old New York Evening Post Building: The Old "New York Evening Post" Building is the former office and printing plant of the "New York Evening Post" newspaper located at 20 Vesey Street between Church Street and Broadway in the Financial District of Manhattan, New York City.  It was built in 1906-07 and was designed by architect Robert D. Kohn for Oswald Garrison Villard, who owned the Post at the time, and is considered to be "one of the few outstanding Art nouveau buildings" ever constructed in the United States.

Leonard Macaluso: Leonard "Iron Legs" Macaluso was an American football player and wrestler.  He played fullback for Colgate University from 1928 to 1930.  Macaluso was the leading scorer among the major college teams in 1930 (145 points) and was one of two players (Ben Ticknor was the other) to be virtually unanimous choices as a first-team All-Eastern player.  He was also selected as a first-team All-American in 1930 by the Associated Press, United Press, Colliers, International News Service (INS), "New York Evening Post", and "New York Sun"."  Macaluso later became a professional wrestler, competing under the name "Iron Legs" Macaluso.

New York Evening Post Building: The New York Evening Post Building, also known as the New York Post Building or the Post Towers, is a historic commercial building located in Lower Manhattan, New York City, New York.  The building was designed by noted architect Horace Trumbauer and built in 1926.

New York Post: The New York Post is an American daily newspaper that is primarily distributed in New York City and its surrounding area.  It is the 13th-oldest newspaper in the United States, and it had the sixth-highest circulation in 2009.  Established in 1801 by federalist and Founding Father Alexander Hamilton, it became a respected broadsheet in the 19th century, under the name New York Evening Post.  The modern version of the paper is published in tabloid format.

Edwin Lawrence Godkin: Edwin Lawrence Godkin (October 2, 1831 – May 21, 1902) was an Irish-born American journalist and newspaper editor.  He founded "The Nation" and was the editor-in-chief of the "New York Evening Post" from 1883 to 1899.

Burton J. Hendrick: Burton Jesse Hendrick (December 8, 1870 – March 23, 1949), born in New Haven, Connecticut, was an American author.  While attending Yale University, Hendrick was editor of both The Yale Courant and The Yale Literary Magazine.  He received his BA in 1895 and his master's in 1897 from Yale.  After completing his degree work, Hendrick became editor of the New Haven Morning News.  In 1905, after writing for "The New York Evening Post" and The New York Sun, Hendrick left newspapers and became a "muckraker" writing for McClure's Magazine.  His "The Story of Life-Insurance" exposé appeared in McClure's in 1906.  Following his career at McClure's, Hendrick went to work in 1913 at Walter Hines Page's "World's Work" magazine as an associate editor.  In 1919, Hendrick began writing biographies, when he was the ghostwriter of Ambassador Morgenthau's Story for Henry Morgenthau, Sr.

Raymond H. Torrey: Raymond Hezekiah Torrey (July 15, 1880 – July 15, 1938) was the author of weekly columns, "Outings" and "The Long Brown Path" in the "New York Evening Post" in the 1920s and 1930s.  The column played a major role in the development of the 2100 mi Appalachian Trail, the Long Path and the popularity of hiking generally.  He was a founding member of the New York–New Jersey Trail Conference and one of the authors of the first edition of the "New York Walk Book".  He had extensive scientific knowledge, writing about everything from the short-billed marsh wren to marine fossils and lichens; he could identify over 700 plants.  He was secretary of the Association for the Preservation of the Adirondacks, and also secretary of the American Scenic and Historic Preservation Society.

Question: The Old "New York Evening Post" Building is the former office and printing plant of the "New York Evening Post" newspaper, located in which city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "building_name": {
      "type": "string",
      "description": "The name of the building."
    },
    "location_city": {
      "type": "string",
      "description": "The city where the building is located."
    },
    "location_district": {
      "type": "string",
      "description": "The specific district within the city where the building is located."
    },
    "building_purpose": {
      "type": "string",
      "description": "The primary purpose or function of the building."
    }
  },
  "required": [
    "building_name",
    "location_city",
    "location_district",
    "building_purpose"
  ],
  "additionalProperties": false
}
