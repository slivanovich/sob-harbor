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
Beverley Daurio: Beverley Daurio (born 1953) is a Canadian writer and editor.  Formerly editor-in-chief of "Poetry Canada Review" and editor and publisher of "Paragraph: the Canadian Fiction Review" (formerly Cross Canada Writers Quarterly owned by Ted Plantos), she is currently editor-in-chief of The Mercury Press.  Books edited by Beverley Daurio have won or been shortlisted for numerous awards, including the Governor General's Award, City of Toronto Book Award, Books in Canada First Novel Award, the Arthur Ellis Award from the Crime Writers of Canada, and many others.  Her short fiction has been published in Canada, Australia, the United States, Romania, and England, and her poetry, reviews, and literary essays have been widely published (including "The Globe and Mail", "Books in Canada", "The Malahat Review" and many other venues.  "If Summer Had a Knife" was shortlisted for the Gerald Lampert Award.  She has served on the boards of directors of various organizations, including the Literary Press Group and the Book and Periodical Council, and has been the recipient of grants in writing from the Canada Council for the Arts, the Ontario Arts Council, and the Toronto Arts Council, as well as the Barbara Deming Memorial Award (US).  She was a founder of the Canadian Poetry Association in 1985. She has designed and taught creative writing courses at George Brown College, the Kingston School of Writers, and This Ain't the Rosedale Library, as well as run day-long workshops for high-school students, and has attended writing residencies in Canada and the United States (most recently at the Atlantic Centre for the Arts in Florida, studying with Master Artist William Gass).  In multidisciplinary art, she has worked with choreographer and dancer Sheila Muir, choreographer Ted Fox, and with visual artist Sheila Gregory.

Roy Thomas: Roy William Thomas, Jr. (born November 22, 1940) is an American comic book writer and editor, who was Stan Lee's first successor as editor-in-chief of Marvel Comics.  He is possibly best known for introducing the pulp magazine hero Conan the Barbarian to American comics, with a series that added to the storyline of Robert E. Howard's character and helped launch a sword and sorcery trend in comics.  Thomas is also known for his championing of Golden Age comic-book heroes – particularly the 1940s superhero team the Justice Society of America – and for lengthy writing stints on Marvel's "X-Men" and "The Avengers", and DC Comics' "All-Star Squadron", among other titles.

Stan Lee's Mutants, Monsters &amp; Marvels: Stan Lee's Mutants, Monsters & Marvels is a 2002 American documentary film produced by Creative Light Entertainment consisting of an interview of Marvel Comics publisher Stan Lee by film director Kevin Smith.  The two talk about Lee's life, his marriage with Joan Lee, the 2002 "Spider-Man" film, and Spider-Man comics.  Lee refers to Marvel Comics character J. Jonah Jameson as "the version so many people had of me."  The interview was filmed in February 2002 in Santa Monica, California at a comic book store.  The result was a nearly two-hour-long film.  The documentary was included in a four-disc release of the 2002 "Spider-Man" film.

Colleen Doran: Colleen Doran (born July 24, 1964) is an American writer/artist and cartoonist.  She illustrated hundreds of comics, graphic novels, books and magazines, including the autobiographical graphic novel of Marvel Comics editor and writer Stan Lee entitled "Amazing Fantastic Incredible Stan Lee", which became a "New York Times" bestseller.  She adapted and did the art for the short story "Troll Bridge" by Neil Gaiman, which also became a "New York Times" bestseller.  Her books have received Eisner, Harvey, and International Horror Guild Awards.

Vincent Fago: Vincenzo Francisco Gennaro Di Fago ( ; November 28, 1914 – June 13, 2002), known professionally as Vince Fago, was an American comic-book artist and writer who served as interim editor of Timely Comics, the Golden Age predecessor of Marvel Comics, while editor Stan Lee did his World War II service.

Stan Lee: Stan Lee (born Stanley Martin Lieber , December 28, 1922) is an American comic-book writer, editor, film executive producer, and publisher.  He was formerly editor-in-chief of Marvel Comics, and later its publisher and chairman before leaving the company to become its chairman emeritus, as well as a member of the editorial board.

Leonard Downie Jr.: Leonard "Len" Downie Jr. (born May 1, 1942), the American journalist, was Executive Editor of "The Washington Post" from 1991 to 2008.  He worked in the Post newsroom for 44 years as Executive Editor, Managing Editor, National Editor, London correspondent, Assistant Managing Editor for Metropolitan News, Deputy Metropolitan Editor, and as an award winning investigative and local reporter.  Downie became Executive Editor upon the retirement of Ben Bradlee.  During Downie's tenure as Executive Editor, The Washington Post won 25 Pulitzer Prizes, more than any other newspaper has won during the term of a single Executive Editor, including three Pulitzer Gold Medals for Public Service.  Downie currently serves as Vice President At Large at the Washington Post Company, as Weil Family Professor of Journalism at the Walter Cronkite School of Journalism and Mass Communication at Arizona State University, and as a member of several advisory boards associated with journalism and public affairs.

Harpies (film): Harpies (or Stan Lee's Harpies) is a Sci Fi Pictures original film directed by Josh Becker.  Stan Lee is the executive producer.  The film began pre-production under the working title "The Harpy" on June 26, 2006 and first aired on June 23, 2007.  The movie was shot in Bulgaria.

Geoff Edgers: Geoff Edgers (born 1970) is an American journalist and writer whose work includes reporting for "The Washington Post" and "The Boston Globe" as well as producing and starring in the 2010 music documentary "Do It Again".  His articles have appeared in magazines such as "GQ" and "Wired", and he has worked as a reporter for several newspapers, including the "Boston Phoenix", "Raleigh News and Observer", "The Boston Globe", and "The Washington Post".  Edgers has also published two children's books on Elvis, The Beatles, Stan Lee and contributed to WBUR Boston.  In 2013, he hosted a Travel Channel reality TV series called "Edge of America", and in June 2013 he was awarded a New England Emmy for work on a video for "The Boston Globe".  Edgers joined "The Washington Post" in September 2014 as the paper's national arts reporter and currently hosts the military history series "Secrets of the Arsenal" on the American Heroes Channel.

Marcus McLaurin: Marcus McLaurin is an American comic-book writer and editor known for developing and editing the influential Marvel Comics series "Marvels".

Question: Geoff Edgers, is an American journalist and writer whose work includes reporting for "The Washington Post", Edgers has also published two children's books on Elvis, The Beatles, Stan Lee and contributed to WBUR Boston, Stan Lee, is an American comic-book writer, editor, film executive producer, and publisher, and formerly editor-in-chief, of which organization?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person in question."
    },
    "role": {
      "type": "string",
      "description": "The specific role held by the person."
    },
    "organization_name": {
      "type": "string",
      "description": "The name of the organization where the role was held."
    },
    "is_current_role": {
      "type": "boolean",
      "description": "Indicates if the role is currently held by the person."
    }
  },
  "required": [
    "person_name",
    "role",
    "organization_name",
    "is_current_role"
  ],
  "additionalProperties": false
}
