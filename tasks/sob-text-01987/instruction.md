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
Cross My Heart (novel): Cross My Heart is the 21st novel in the Alex Cross series all written by author James Patterson.  The novel takes place after "Alex Cross, Run", in which Alex tries contemplating a life outside the Metro Police, after the apparent death of Ava, an orphan girl they took in.  It was initially not planned by Patterson, but was later confirmed to be in the works.  The novel will once again feature Metro Police detective Alex Cross.  "Cross My Heart" will be released 20 years after the original novel, "Along Came a Spider" was released.  The novel's events, having ended on a cliffhanger, were continued in the next novel, Hope to Die.

Cyrus Saatsaz: Cyrus Saatsaz is a journalism professor at the University of Houston and was formerly an instructor in the Journalism & Media Studies department at San Diego State University, the host of WaXed a surf talk show radio show that aired on ESPN 1700 in Southern California, is the author of "Dogwild & Board: Stories, Interviews and Musings from a Surf Journalist", and is a writer for The Huffington Post and GrindTV.com which is associated with Yahoo Sports.  Saatsaz was an editor with USA Today for nine years.  Saatsaz hosted and was Editor-in-Chief of The Extreme Scene, the world's first action sports radio talk show.  In addition to writing for The Huffington Post, Saatsaz is an award winning journalist, having been published in newspapers, magazines, books and websites including the San Francisco Chronicle and its official website SFGate. com, USA Today, AOL.com, Future Snowboarding Magazine, Fuel.TV, The Great Book of San Francisco/Bay Area Sports Lists, and many more.  Saatsaz is the founder of a surf shop/bookstore/art gallery in San Francisco called San Francisco Surf Company.  Saatsaz also worked for KNBR 680/1050 in San Francisco and The Mighty 1090 and ESPN 1700 in San Diego for 14 years, serving as a sports anchor, host, Creative Director and Executive Producer.

James Patterson: James Brendan Patterson (born March 22, 1947) is an American author and philanthropist.  Among his works are the "Alex Cross", "Michael Bennett", "Women's Murder Club", "Maximum Ride", "Daniel X", "NYPD Red", "Witch and Wizard", and "Private" series, as well as many stand-alone thrillers, non-fiction and romance novels.  His books have sold more than 300 million copies and he was the first person to sell 1 million e-books.  In 2016, Patterson topped "Forbes"'s list of highest-paid authors for the third consecutive year, with an income of $95 million.  His total income over a decade is estimated at $700 million.

Simenona Martinez: Simenona Martinez is an American actress, singer-songwriter and film director from Los Angeles, California.  She made her television debut in on the WB20 in San Francisco, California.  She is most well known for her work on the Disney Channel's Playhouse Disney show Behind the Ears and for her role in "Alex Cross" alongside Tyler Perry.

Alex Cross (film): Alex Cross is a 2012 American action crime-thriller film directed by Rob Cohen and starring Tyler Perry as the title character and Matthew Fox as the villain Picasso.  The adapted screenplay was written by Marc Moss and Kerry Williamson.  This is the third film appearance of the character Alex Cross, the lead of a series of novels by James Patterson.  Cross was previously portrayed by Morgan Freeman in "Kiss the Girls" (1997) and "Along Came a Spider" (2001).  In 2010, Idris Elba was hired to play Cross, but was replaced by Perry.  Filming took place in 2011, and "Alex Cross" was released on October 19, 2012 in the United States and Canada.

Ruth Asawa's San Francisco Fountain: Ruth Asawa's San Francisco Fountain, or sometimes simply San Francisco Fountain, is a 1970 bronze sculpture and fountain by Ruth Asawa, located outside the Grand Hyatt San Francisco in downtown San Francisco, California, in the United States.  The cylinder-shaped sculpture, which serves as the outer wall of the fountain basin, features bas-relief scenes of San Francisco, "whimsically interrelated".  It measures approximately 90 in tall, with a diameter of 193 in , and is set into a base of brick stairs.  Albert Lanier served as the architect; credited assistants include Aiko Asawa, Haru Awara, Mae Lee, Mei Mei, Hector Villanueva, and Sally Woodbridge.

Women's Murder Club (TV series): Women's Murder Club is an American police procedural and legal drama, which aired on ABC from October 12, 2007, to May 13, 2008.  The series is set in San Francisco, California, and is based on the series of novels by the same name written by James Patterson.  Series creators Elizabeth Craft and Sarah Fain also served as executive producers alongside Patterson, Joe Simpson, Brett Ratner, and R. Scott Gemmill.  The latter also served as showrunner, with Gretchen J. Berg and Aaron Harberts co-executive producing.  The pilot was directed by Scott Winant.

Alex Cross, Run: Alex Cross, Run is the 20th novel in the "Alex Cross" series written by American author James Patterson.  The novel focuses on the protagonist, detective Alex Cross, who must solve three cases at once with the whole city in a frenzy.

Alex Cross's Trial: Alex Cross's Trial is the 15th novel in James Patterson's "Alex Cross" series.  It follows "Cross Country" in the series, and comes before his novel "I, Alex Cross".  It is written by Patterson and Richard DiLallo, and its premise is that it is a book written by Alex Cross.

Alex Cross (novel series): Alex Cross is a crime, mystery, and thriller novel series written by James Patterson.  The series focuses on the protagonist—African-American Metropolitan Police Department detective and father Alex Cross—as he faces threats to his family and the city of Washington, D.C..  Supporting characters include two of Cross's children, Damon, and Janelle, as well as his grandmother Nana Mama.  The series is usually narrated in first-person perspective by Alex Cross, and occasionally from the villains' point of view in third-person.

Question: What series set in San Francisco, California was written by the author of Alex Cross? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author who wrote the Alex Cross series."
    },
    "author_series": {
      "type": "array",
      "description": "A list of series written by the identified author.",
      "items": {
        "type": "string"
      }
    },
    "series_set_in_san_francisco": {
      "type": "array",
      "description": "A list of series mentioned in the context that are set in San Francisco, California.",
      "items": {
        "type": "string"
      }
    },
    "matching_series": {
      "type": "string",
      "description": "The series that is both written by the author of Alex Cross and set in San Francisco, California."
    }
  },
  "required": [
    "author_name",
    "author_series",
    "series_set_in_san_francisco",
    "matching_series"
  ],
  "additionalProperties": false
}
