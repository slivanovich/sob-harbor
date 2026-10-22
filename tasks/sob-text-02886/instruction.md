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
David D. Busch: David D. Busch is a photographer and well-known award-winning author of more than 200 books with a total of more than two million copies in print, and thousands of photography- and technology-related articles for "Popular Photography", "Rangefinder", "Professional Photographer", "Computer Shopper", and other magazines.  He is best known for the classic imaging handbook "Digital Photography All in One Desk Reference for Dummies", which, along with "Mastering Digital Photography", was named by About.com as the top two of five recommended books for digital photography beginners.  He is the main author and series editor of "David Busch's Quick Snap Guides", "David Busch's Pro Secrets", and "David Busch's Guides to Digital SLR Photography".

Selena Roberts: Selena Roberts (born May 16, 1966 in Live Oak, Florida) is an American best-selling author, sportswriter, and digital entrepreneur.  Previously, she was a senior writer for "Sports Illustrated" and a columnist for "The New York Times".  Roberts began her career as a beat writer for the Minnesota Vikings at the "Minneapolis Star Tribune" and for the Orlando Magic and Tampa Bay Buccaneers at the "Orlando Sentinel".  She received a B.A. degree in journalism from Auburn University in 1988 where she was a sports editor for the university paper "The Plainsman".  She also made frequent appearances on the ESPN talk show "The Sports Reporters".  In a February 7, 2009 article on SI.com that quickly made the cover of "Sports Illustrated", Roberts revealed that Yankees third baseman Alex Rodriguez tested positive for steroids in 2003.

Sports Illustrated Kids: Sports Illustrated Kids (SI Kids, trademarked Sports Illustrated KIDS, sometimes Sports Illustrated for Kids) is a monthly spin-off of the weekly U.S. sports magazine "Sports Illustrated".  "SI Kids" was launched in January 1989 and includes sports coverage with less vocabulary and emphasis on humor.  The magazine's secondary purpose is to market sports to children.

Herbert Keppler: Herbert "Burt" Keppler (April 21, 1925 – January 4, 2008) was an American photographer, journalist, author and consultant.  His career spanned 57 years, including 37 at "Modern Photography" and two decades at "Popular Photography".  He wrote monthly columns and served in the former magazine as Editorial Director and Publisher, and in the latter magazine as Vice President and Publishing Director.

Sports Illustrated for Women: Sports Illustrated Women (previously called Sports Illustrated for Women) and also known as SI Women, was a bimonthly sports magazine covering (according to its statement of purpose) "the sports that women play and what they want to follow, from basketball to tennis, soccer to volleyball, field hockey to ice hockey and figure skating and more.  It featured real athletes, told their real stories and gave the real scoop on women's sports.  "Sports Illustrated for Women" was published by Time Inc." It ran for 20 issues, between March 2000 and November 2002, targeting an audience of women, 18–34 years old, with "a passion for sports."

Popular Photography: Popular Photography, formerly known as Popular Photography & Imaging, also called Pop Photo, was a monthly American consumer magazine that at one time had the largest circulation of any imaging magazine, with an editorial staff twice the size of its nearest competitor.

Ailladie: Ailladie is an area on the coast of The Burren in County Clare, Ireland, which is one of Ireland's most highly regarded rock-climbing locations.  It is also a popular location for beach-angling competitions, and, with its cliffs and view of Aran, is a popular photography stop for tourist coaches travelling through west Clare.  It is situated between the villages of Fanore to the north, and Doolin to the south.

F.M. Norris House: The F.M. Norris House, also known as the Patton House and the Gerard Photography Studio, was a historic building located in Mason City, Iowa, United States.  Fred Magee Norris (1864-1938) served two terms as the mayor of the city.  He was married to Elizabeth (Atkinson) Norris (1866-1933).  They had Chris Rye build this Prairie School house for them.  While Rye built some of Walter Burley Griffin's designs, it is possible that he designed this house himself.  It featured a horizontal emphasis, wide eaves, broad hip roof, and stucco walls.  The building was altered by Jerome J. Gerard (1913-2010) for his photography studio.  In addition to his photographic work, he wrote for the magazine "Popular Photography" for 20 years.  The house was listed on the National Register of Historic Places in 1980.  It has subsequently been torn down.

Larry Johnson (author): Larry Johnson (born in Albuquerque, New Mexico) is an American author and former employee of the Alcor Life Extension Foundation (Alcor), a cryonics company for whom he once served as chief operating officer.  He received notoriety with the release of the August 13, 2003 issue of "Sports Illustrated".  "Sports Illustrated" sportswriter Tom Verducci, along with Johnson's input, published an article about “What Really Happened to Ted Williams?"  Immediately following the "Sports Illustrated" article, Johnson agreed to an interview with Diane Sawyer of Good Morning America.

Heinz Kluetmeier: Heinz Kluetmeier (born 1942) is a German-born American sports photographer for "Sports Illustrated".  He has covered every Olympic Games for the magazine since the 1972 Munich games except one, and has over 100 "Sports Illustrated" cover photographs to his credits.  He has served two stints as the magazine's director of photography and received the Lucie Award for outstanding achievement in sports photography in October 2007.

Question: Sports Illustrated Kids and Popular Photography are considered to be what kind of production?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "publication_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the publications identified in the question."
    },
    "production_type": {
      "type": "string",
      "description": "The common type of production for the listed publications."
    },
    "description_source": {
      "type": "string",
      "description": "Indicates where the information about the production type was found in the context."
    }
  },
  "required": [
    "publication_names",
    "production_type",
    "description_source"
  ],
  "additionalProperties": false
}
