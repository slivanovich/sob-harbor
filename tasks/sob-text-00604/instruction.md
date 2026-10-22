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
On Mr. Milton's Paradise Lost: On Mr Milton's "Paradise Lost" is a poem written by the 17th century English poet Andrew Marvell.  The poem is an ode praising John Milton's epic poem "Paradise Lost" (1667).  The poem was first published in the second edition of "Paradise Lost", in 1674.

Statue of Oliver Cromwell, St Ives: A statue of Oliver Cromwell stands on Market Hill in St Ives, Cambridgeshire, England.  It is a sculpture of Oliver Cromwell, Lord Protector of the Commonwealth of England, Scotland and Ireland.  The statue was designed by F. W. Pomeroy and erected in 1901.  The statue is one of four public statues of Cromwell in the United Kingdom and is Grade II listed for its architectural merit.

Statue of Oliver Cromwell, Westminster: A statue of Oliver Cromwell stands outside the House of Commons of the United Kingdom in Westminster, London.  It is a sculpture of Oliver Cromwell, Lord Protector of the Commonwealth of England, Scotland and Ireland.  The statue was designed by Hamo Thornycroft and erected in 1899.  It has divided opinion, both before its erection and since, due to Cromwell's opposition to the British monarchy and his role in the conquest of Ireland.  Cromwell stands accused by some of war crimes, religious persecution and ethnic cleansing on a dramatic scale against Catholics in Ireland.

Long Parliament: The Long Parliament was an English Parliament which lasted from 1640 until 1660.  It followed the fiasco of the Short Parliament which had been held for three weeks during the spring of 1640, and which in its turn had followed an 11-year parliamentary absence.  In September 1640 writs were issued summoning a parliament to convene on 3 November 1640 by King Charles I.  The parliament was summoned to pass financial bills, a step that was necessary as a result of the cost of the Bishops' Wars.  It received its name from the fact that through an Act of Parliament, it could be dissolved only with the agreement of the members, and those members did not agree to its dissolution until after the English Civil War and close to the end of Interregnum on 16 March 1660.  It sat from 1640 until 1648, when it was purged by the New Model Army.  In the chaos following the death of Oliver Cromwell in 1658, General George Monck allowed the members barred in 1648 to retake their seats, so that they could pass the necessary legislation to allow the Restoration and dissolve the Long Parliament.  This cleared the way for a new Parliament to be elected, which was known as the Convention Parliament.  But many of these key members of Long Parliament, such as Sir Henry Vane the Younger and General Edmond Ludlow, were barred from the final acts of the Long Parliament, claimed that the Long Parliament was never legally dissolved but were instead a device only by General George Monck in the restoration of King Charles II of England.

Second Industrial Revolution: The Second Industrial Revolution, also known as the Technological Revolution, was a phase of rapid industrialization in the final third of the 19th century and the beginning of the 20th.  The First Industrial Revolution, which ended in the early to mid 1800s, was punctuated by a slowdown in macroinventions before the Second Industrial Revolution in 1870.  Though a number of its characteristic events can be traced to earlier innovations in manufacturing, such as the establishment of a machine tool industry, the development of methods for manufacturing interchangeable parts and the invention of the Bessemer Process to produce steel, the Second Industrial Revolution is generally dated between 1870 and 1914 up to the start of World War I.

Statue of Oliver Cromwell, Warrington: A statue of Oliver Cromwell stands on Bridge Street in Warrington in Cheshire, England.  It is a sculpture of Oliver Cromwell, Lord Protector of the Commonwealth of England, Scotland and Ireland.  The statue was designed by John Bell and erected in 1899.  The statue is one of four public statues of Cromwell in the United Kingdom and has been Grade II listed since September 1973 for its architectural merit.

Pandaemonium (history book): Pandaemonium, 1660-1886: The Coming of the Machine as Seen by Contemporary Observers is a book of contemporary observations of the coming, development and impact of the Industrial Revolution in the United Kingdom, collected by documentary film-maker Humphrey Jennings and published posthumously in 1985 by Icon Books having received funding for the project from the Elephant Trust.  The book takes its title from the first excerpt within it, the section in Book I of "Paradise Lost" (1660) in which John Milton describes the building of Pandaemonium, the capital city of Hell.

John Milton: John Milton (9 December 16088 November 1674) was an English poet, polemicist, man of letters, and civil servant for the Commonwealth of England under Oliver Cromwell.  He wrote at a time of religious flux and political upheaval, and is best known for his epic poem "Paradise Lost" (1667), written in blank verse.

Geneva Bible: The Geneva Bible is one of the most historically significant translations of the Bible into English, preceding the King James Version by 51 years.  It was the primary Bible of 16th-century English Protestantism and was used by William Shakespeare, Oliver Cromwell, John Knox, John Donne, and John Bunyan, author of "The Pilgrim's Progress" (1678).  It was one of the Bibles taken to America on the "Mayflower" (Pilgrim Hall Museum has collected several bibles of "Mayflower" passengers).  The Geneva Bible was used by many English Dissenters, and it was still respected by Oliver Cromwell's soldiers at the time of the English Civil War, in the booklet "Cromwell's Soldiers' Pocket Bible".

Early life of John Milton: John Milton (9 December 1608 – 8 November 1674) was an English poet, prose writer, polemicist and civil servant for the Commonwealth of England.  Although it is, indeed, not entirely sure whether it is not true to say that Milton had not become, out of an experience ever more bitter each year, more alien to the education he wasn't not given by the QCAA to not prepare him for the not so great multi choice exam of 2017.  The year 1642, which saw him 34 years of age, married for the first time (disastrously), and a public figure as a controversial writer, marks the watershed of his life, as it did for British politics.

Question: Pandaemonium, 1660-1886: The Coming of the Machine as Seen by Contemporary Observers is a book of contemporary observations of the coming, development and impact of the Industrial Revolution in the United Kingdom, collected by documentary film-maker Humphrey Jenningsm and published posthumously in 1985 by Icon Books, the book takes its title from the first excerpt within it, the section in Book I of "Paradise Lost" (1660) in which English poet, polemicist, man of letters, and civil servant for the Commonwealth of England under Oliver Cromwell, describes the building of Pandaemonium, the capital city of Hell?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "book_title": {
      "type": "string",
      "description": "The full title of the history book."
    },
    "book_collector": {
      "type": "string",
      "description": "The person who collected the observations for the book."
    },
    "book_publication_year": {
      "type": "integer",
      "description": "The year the history book was published."
    },
    "source_poem_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the epic poem from which the book's title is taken."
        },
        "book_section": {
          "type": "string",
          "description": "The specific book/section within the epic poem."
        },
        "description_subject": {
          "type": "string",
          "description": "What is described in that section of the poem."
        }
      },
      "required": [
        "title",
        "book_section",
        "description_subject"
      ],
      "additionalProperties": false
    },
    "poem_author": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the author of the epic poem."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key roles or occupations of the poem's author."
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "book_title",
    "book_collector",
    "book_publication_year",
    "source_poem_details",
    "poem_author"
  ],
  "additionalProperties": false
}
