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
Lego Harry Potter: Lego "Harry Potter" is a Lego theme based on the films of the "Harry Potter" series.  Lego models of important scenes, vehicles and characters were made for the first six films and all the books released.  The first sets appeared in 2001, to coincide with the release of the first film "Harry Potter and the Philosopher's Stone" (Harry Potter and the Sorcerer's Stone in the United States).  Subsequent sets were released alongside the new films, until Harry Potter and the Order of the Phoenix.  The line then went dormant for three years.  It is unknown if the theme will again be revived to coincide with future installations in the Harry Potter franchise, such as the film Fantastic Beasts and Where to Find Them.

Harry Potter and the Chamber of Secrets (film): Harry Potter and the Chamber of Secrets is a 2002 British-American fantasy film directed by Chris Columbus and distributed by Warner Bros.  Pictures.  It is based on the novel of the same name by J. K. Rowling.  The film is the second instalment in the long-running "Harry Potter" film series.  It was written by Steve Kloves and produced by David Heyman.  Its story follows Harry Potter's second year at Hogwarts School of Witchcraft and Wizardry as the Heir of Salazar Slytherin opens the Chamber of Secrets, unleashing a monster that petrifies the school's denizens.  The film stars Daniel Radcliffe as Harry Potter, with Rupert Grint as Ron Weasley, and Emma Watson as Hermione Granger.  The film is also the last film to feature Richard Harris as Professor Albus Dumbledore, due to his death that same year.

Miriam Margolyes: Miriam Margolyes, {'1': ", '2': ", '3': ", '4': "} ( ; born 18 May 1941) is an English character actress and voice artist.  Her earliest roles were in theatre and after several supporting roles in film and television she won a BAFTA Award for her role in "The Age of Innocence" (1993) and went on to take the role of Professor Sprout in the "Harry Potter" film series.

Danielle Elizabeth Tumminio: Danielle Elizabeth Tumminio is an Episcopal priest, theologian, a certified life coach and spinning instructor, and the author of "God and Harry Potter at Yale: Teaching Faith and Fantasy Fiction in an Ivy League Classroom".  She was the instructor of the "Christian Theology and Harry Potter" seminar at Yale University in the spring of 2008; in 2011, she repeated the course at Tufts University.  Tumminio has also presented material on the intersection between theology and the Harry Potter series at the Infinitus Symposium in Orlando, Florida in 2010, the Portus Symposium in Dallas, Texas, in the summer of 2008, and she chaired the panel on Harry Potter and Religion at the 2008 American Academy of Religion conference.  Her teaching has been praised by Harry Potter commentator John Granger on his Hogwarts Professor website.

Bottersnikes and Gumbles (TV series): Bottersnikes and Gumbles is a British-Australian animated television series that aired on 7TWO in Australia and CBBC in the United Kingdom.  The cast includes Jason Callender, Richard Grieve, Jeff Rawle, Kathryn Drysdale and Miriam Margolyes.  It was released on Netflix in North America on 19 August 2016; which was re-dubbed with American accents.

Parodies of Harry Potter: The immense popularity and wide recognition of J. K. Rowling's Harry Potter fantasy series has led to its being extensively parodied, in works spanning nearly every medium.  The franchise holds the record for the most fan fiction parodies, at over 900.000 Some self-described parodies have been targeted by Rowling and her publishers as plagiarism, while others have sold hundreds of thousands of copies without any threat of legal sanction.  Misinterpretations of "Harry Potter" parodies have sparked at least two urban legends.  Many "Harry Potter" parodies are self-published; others are put out as part of major comic productions, such as "Mad", "The Simpsons", "South Park", "Saturday Night Live" and "Robot Chicken", all of which have parodied "Harry Potter" several times.  Rowling has also been parodied (and parodied herself) in a number of instances.

Harry Potter (film series): Harry Potter is a British-American film series based on the "Harry Potter" novels by author J. K. Rowling.  The series is distributed by Warner Bros. and consists of eight fantasy films, beginning with "Harry Potter and the Philosopher's Stone" (2001) and culminating with "Harry Potter and the Deathly Hallows – Part 2" (2011).  A spin-off prequel series will consist of five films, starting with "Fantastic Beasts and Where to Find Them" (2016).  The "Fantastic Beasts" films mark the beginning of a shared media franchise known as J. K. Rowling's Wizarding World.

Warner Bros. Entertainment Inc. v. RDR Books: Warner Bros.  Entertainment, Inc. and J. K. Rowling v. RDR Books, 575 F.Supp.2d 513 (SDNY 2008) is a copyright lawsuit brought on 31 October 2007 by the media company Warner Bros. and "Harry Potter" author J. K. Rowling against RDR Books, an independent publishing company based in Muskegon, Michigan.  Lawyers for Rowling and Time Warner argued that RDR's attempt to publish for profit a print facsimile of "The Harry Potter Lexicon", a free online guide to the "Harry Potter" fictional universe, constituted an infringement of their copyright and was not protected by the affirmative defense of fair use.  The trial was held from 14–17 April 2008 in the United States District Court for the Southern District of New York.  In September 2008, the court ruled in Rowling's favor, and publication of the book was blocked.  In 2009, RDR Books released an edited volume, eliminating the problematic long quotes found to be infringing.

Harry Potter and the Philosopher's Stone: Harry Potter and the Philosopher's Stone is the first novel in the "Harry Potter" series and J. K. Rowling's debut novel, first published in 1997 by Bloomsbury.  It was published in the United States as Harry Potter and the Sorcerer's Stone by Scholastic Corporation in 1998.  The plot follows Harry Potter, a young wizard who discovers his magical heritage as he makes close friends and a few enemies in his first year at the Hogwarts School of Witchcraft and Wizardry.  With the help of his friends, Harry faces an attempted comeback by the dark wizard Lord Voldemort, who killed Harry's parents, but failed to kill Harry when he was just 15 months old.

Harry Potter and the Deathly Hallows: Harry Potter and the Deathly Hallows is the seventh and final novel of the "Harry Potter" series, written by British author J. K. Rowling.  The book was released on 21 July 2007, ten years after publication of "Harry Potter and the Philosopher's Stone" (1997), by Bloomsbury Publishing in the United Kingdom, in the United States by Scholastic, and in Canada by Raincoast Books, ending the series that began in 1997 with the publication of "Harry Potter and the Philosopher's Stone".  The novel chronicles the events directly following "Harry Potter and the Half-Blood Prince" (2005), and the final confrontation between the wizards Harry Potter and Lord Voldemort, as well as revealing the previously concealed back story of several main characters.  The title of the book refers to three mythical objects featured in the story, collectively known as the "Deathly Hallows"—an unbeatable wand, a stone to bring the dead to life, and a cloak of invisibility.

Question: Who played the role of Professor Sprout in the "Harry Potter" films and also played in Botternikes and Gumble, an animated series that originally aired in Australia and the U.K., but later came re-dubbed to Netflix in the United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "harry_potter_role": {
      "type": "string",
      "description": "The character played by the actress in the Harry Potter film series."
    },
    "animated_series_details": {
      "type": "object",
      "properties": {
        "series_name": {
          "type": "string",
          "description": "The name of the animated series."
        },
        "original_air_regions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Regions where the animated series originally aired."
        },
        "netflix_release_region": {
          "type": "string",
          "description": "The region where the series was released on Netflix."
        },
        "netflix_release_year": {
          "type": "integer",
          "description": "The year the series was released on Netflix."
        }
      },
      "required": [
        "series_name",
        "original_air_regions",
        "netflix_release_region",
        "netflix_release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "harry_potter_role",
    "animated_series_details"
  ],
  "additionalProperties": false
}
