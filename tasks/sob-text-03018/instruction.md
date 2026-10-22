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
Walt Disney (film): Walt Disney is a documentary film created by PBS for the "American Experience" program.  The two-part, four-hour documentary premiered on September 14, 2015 and centers on the life, times and legacy of Walt Disney.  According to Sarah Colt, director of the documentary film, the biggest challenge was "capturing the truth of the man who had such [an] outsized influence and notoriety ... People think they know him but in reality they don't know him ... He was a human being with many layers of complexity."  Rob Lowman, of the "Los Angeles Daily News", described "Disneyesque" as being "synonymous with a specific artistic style and, eventually, a fantasy world."  Richard Sherman, a Disney songwriter, recalled that "Disney was never driven by a desire for wealth or fame.  He wanted to be seen as a master storyteller ... He got great joy out of making people happy with his movies."

Walt Disney World Company: Walt Disney World Company was created in 1967 as the company that initially owned and operated Walt Disney World near Orlando, Florida.  The resort opened in 1971 and the land was owned by Walt Disney World Company, Walt Disney Travel Company, and Walt Disney World Hospitality and Recreation Corporation.  In 2009 the name was changed to Walt Disney Parks and Resorts division of The Walt Disney Company.

The Walt Disney Company Italy: The Walt Disney Company Italia S.r.l. (formerly called The Walt Disney Company Italia S.p.A) is The Walt Disney Company's Italian division and one of The Walt Disney Company's European divisions.  The company was founded on 8 May 1938 as Creazioni Walt Disney S.A.I.  The company owns and operates Disney Channel Italy, Disney in English, and more.  Comics are also published by the company as well.

Walt Disney World Dolphin: The Walt Disney World Dolphin is a resort hotel designed by architect Michael Graves located between Epcot and Disney's Hollywood Studios in the Walt Disney World Resort in Bay Lake, Florida, next to Disney's BoardWalk Resort area.  It opened on June 1, 1990 and is joined to its sister hotel, the Walt Disney World Swan (also designed by Graves) by a palm-tree lined covered walkway crossing a lagoon.  The Walt Disney World Swan and Dolphin is a joint venture between the Walt Disney Company, Tishman Hotel Corporation, MetLife and Starwood Hotels and Resorts.  The land the resort occupies is owned by the Walt Disney Company, while the buildings themselves are leased by Disney to the Tishman Hotel Corporation and MetLife but operated by Starwood Hotels & Resorts Worldwide under the Sheraton Hotels brand.  The Walt Disney World Swan and Dolphin are a part of the Walt Disney Collection of resorts; because of this they are Disney branded and guests of the resort have access to special Disney benefits available to Disney Resort Hotel guests only.

Disney Music Group: Disney Music Group (DMG) is the music production arm of Walt Disney Studios, a division of The Walt Disney Company.  The division's subsidiaries consist of two owned record labels—Walt Disney Records, Hollywood Records—and Disney Music Publishing, the publishing entity that administers the company's music, as well as Disney Concerts.  The president of the group is Ken Bunt, who reports to Alan F. Horn, the chairman of The Walt Disney Studios.  It is currently headquartered in the Frank G. Wells Building at The Walt Disney Studios in Burbank.

List of Disney animated shorts: This is a list of animated short films produced by Walt Disney and Walt Disney Animation Studios from 1921 to the present.  This includes films produced at the Laugh-O-Gram Studio which Disney founded in 1921 as well as the animation studio now owned by The Walt Disney Company, previously called the Disney Brothers Cartoon Studio (1923), The Walt Disney Studio (1926), Walt Disney Productions (1929), and Walt Disney Feature Animation (1986).

Walt Disney World Swan: The Walt Disney World Swan is a resort hotel designed by architect Michael Graves located between Epcot and Disney's Hollywood Studios behind Disney's BoardWalk Resort and across from its sister resort, the Walt Disney World Dolphin.  The Swan, which opened January 13, 1990 on Disney property, is a joint venture between the Walt Disney Company, Tishman Hotel Corporation, MetLife and Starwood Hotels and Resorts.  The land the resort occupies is owned by the Walt Disney Company, while the buildings themselves are leased by Disney to the Tishman Hotel Corporation and MetLife and operated by Starwood Hotels & Resorts Worldwide under the Westin brand.  The Walt Disney World Swan and Dolphin are a part of the Walt Disney Collection of resorts, because of this they are Disney branded and guests of the resort have access to special Disney benefits available to Disney Resort Hotel guests only.

The Walt Disney Company: The Walt Disney Company, commonly known as Disney, is an American diversified multinational mass media and entertainment conglomerate, headquartered at the Walt Disney Studios in Burbank, California.  It is the world's second largest media conglomerate in terms of revenue, after Comcast.  Disney was founded on October 16, 1923 – by brothers Walt Disney and Roy O. Disney – as the Disney Brothers Cartoon Studio, and established itself as a leader in the American animation industry before diversifying into live-action film production, television, and theme parks.  The company also operated under the names The Walt Disney Studio and then Walt Disney Productions.  Taking on its current name in 1986, it expanded its existing operations and also started divisions focused upon theater, radio, music, publishing, and online media.

Walt Disney Pictures: Walt Disney Pictures, Inc. is an American film production company and a subsidiary of Walt Disney Studios, owned by The Walt Disney Company.  The division is based at the Walt Disney Studios in Burbank, California, and is the main producer of live-action feature films within the Walt Disney Studios unit.  It took on its current name in 1983.  Today, in conjunction with the other units of Walt Disney Studios, Walt Disney Pictures is classified as one of Hollywood's "Big Six" film studios.  Films produced by Walt Disney Animation Studios and Pixar Animation Studios are also released under this brand.

Manson (film): Manson is a documentary film made in 1973 about Charles Manson and his followers.  It was directed by Robert Hendrickson and Laurence Merrick.

Question: Walt Disney and Manson, are of which genre?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "films": {
      "type": "array",
      "description": "List of films mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          }
        },
        "required": [
          "title"
        ],
        "additionalProperties": false
      }
    },
    "shared_genre": {
      "type": "string",
      "description": "The genre shared by all listed films."
    },
    "genre_is_consistent": {
      "type": "boolean",
      "description": "Indicates if all listed films belong to the same genre."
    }
  },
  "required": [
    "films",
    "shared_genre",
    "genre_is_consistent"
  ],
  "additionalProperties": false
}
