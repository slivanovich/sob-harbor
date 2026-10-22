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
William Hood: William Hood is an art historian and the Mildred C. Jay Professor of Art Emeritus at Oberlin College, where he taught from 1974 through 2007.  Professor Hood taught the history of Italian Renaissance Art in Columbia University's Department of Art History and Archaeology from 2008 through 2010.  He is currently teaching art history seminars at the New York University Institute of Fine Arts.

Jessica Warner: Jessica Warner is an American historian, specializing in the social history of Great Britain in the early modern age.  Her books include "Craze: Gin and Debauchery in an Age of Reason" and "John the Painter: Terrorist of the American Revolution".  The latter book has won praise from fellow historians like Simon Schama and Brenda Maddox.

Donald Kuspit: Donald Kuspit (born March 26, 1935) is an American art critic, poet, and Distinguished Professor Emeritus of art history and philosophy at the State University of New York at Stony Brook and former professor of art history at the School of Visual Arts.  Kuspit is one of America's most distinguished art critics.  He was formerly the A. D. White Professor-at-Large at Cornell University (1991–1997).  He received the Frank Jewett Mather Award for Distinction in Art Criticism in 1983 (given by the College Art Association).  In 1983 he received an honorary doctorate in fine arts from Davidson College, in 1996 from the San Francisco Art Institute, and in 2007 from the New York Academy of Art.  In 1997 the National Schools of Art and Design presented him with a citation for Distinguished Service to the Visual Arts.  In 1998 he received an honorary doctorate of humane letters from the University of Illinois at Urbana-Champaign.  In 2000 he delivered the Getty Lectures at the University of Southern California.  In 2005 he was the Robertson Fellow at the University of Glasgow.  In 2008 he received the Tenth Annual Award for Excellence in the Arts from the Newington-Cropsey Foundation.  In 2014 he was the first recipient of the Gabarron Foundation Award for Cultural Thought.  He has received fellowships from the Ford Foundation, Fulbright Commission, National Endowment for the Arts, National Endowment for the Humanities, Guggenheim Foundation, and Asian Cultural Council, among other organizations.  He has doctorates in philosophy (University of Frankfurt)and art history (University of Michigan), as well as degrees from Columbia University, Yale University, and Pennsylvania State University.  He has also completed the course of study at the Psychoanalytic Institute of the New York University Medical Center.

Claudio Lomnitz: Claudio Lomnitz is the Campbell Family Professor of Anthropology at Columbia University.  Prior to teaching at Columbia, Lomnitz was a Distinguished University Professor of Anthropology and Chair of the Committee on Historical Studies at the New School University.  He served at different points in time as co-director of the University of Chicago's Mexican Studies Program (with Friedrich Katz), Director of the University of Chicago's Latin American Studies Program, and Director of Columbia University's Center for the Study of Ethnicity and Race.  He has also taught at University of Chicago, where he was Professor of History, New York University, El Colegio de México, and Universidad Autónoma Metropolitana Iztapalapa, in Mexico City.  At the New School University, Lomnitz was appointed editor of the academic journal Public Culture, which moved with him to Columbia University in 2006.  He continued to serve as editor until 2011.

Joanna Frueh: Joanna Frueh (b. 1948) is an artist, writer and feminist scholar.  In 2008 she was awarded a Women's Caucus for Art Lifetime Achievement Award.  Her book "Monster Beauty: Building the Body of Love", dealing with the aesthetics of beauty, pleasure and the erotic in everyday life was published by the University of California Press.  Her writing combines theory with autobiography, photography, and poetry to develop these concepts.  She is also a performance artist.  Frueh received her Ph.D. from the University of Chicago in History of Culture.  She is Professor of Art History Emerita at the University of Nevada, Reno, where she served from 1990 to 2006.  Prior to that she was Assistant Professor of art history at Oberlin College, Oberlin, Ohio, (1983-1985) and the University of Arizona, Tucson (1981-1983).  She has authored and edited several books, notably "Erotic Faculties" (University of California Press, 1996) and "Hannah Wilke: A Retrospective" (1989); and coeditor of "Picturing the Modern Amazon" (2000), "Feminist Art Criticism: Art, Identity, Action" (1994), and "Feminist Art Criticism: An Anthology" (1991).  She has written articles and reviews for "Art in America", "Art Journal", "AfterImage", "High Performance Magazine", and "New Art Examiner", among others.

Günsel Renda: Professor Dr. Günsel Renda is a Turkish art historian and a specialist in the history of Ottoman art, especially Ottoman painting and the interactions of European and Ottoman culture.  A graduate of the Department of Art History of Columbia University and Washington University, she was the head of the Department of Art History at the Hacettepe University between 1965 and 2004.  She was an adviser to the Turkish Ministry of Culture and Tourism from 1993-1996 and later president.  She is currently an Adjunct Professor in the Archaeology and History of Art Department at Koç University and resident scholar of the Turkish Cultural Foundation.

Simon Schama: Simon Michael Schama, CBE, FRSL (born 13 February 1945), is an English historian specialising in art history, Dutch history, and French history.  He is a University Professor of History and Art History at Columbia University, New York.  He first came to popular public attention with his history of the French Revolution titled "", published in 1989.  In the United Kingdom, he is perhaps best known for writing and hosting the 15-part BBC television documentary series "A History of Britain" broadcast between 2000 and 2002.

Ann Sutherland Harris: Ann Sutherland Harris (born 1937) is an art historian specializing in Baroque art, Modern art, and in the history of women's art.  She is and educator, having held her first position as Assistant Professor of Art History at Hunter College, City University of New York (1971–1973).  Harris was then hired as Associate Professor at the State University of New York, Albany.  Following that she held the Arthur Kittridge Watson Chair for Academic Affairs at the Metropolitan Museum of Art from 1977–1981.  Harris received a Senior Research Fellowship in 1981-82 from the National Endowment for the Humanities and in 1982, was named the Amon Carter Distinguished visiting Professor of Art History at the University of Texas at Arlington before accepting the position of Mellon Professor of Art History at the University of Pittsburgh.  She is now Professor emerita of Italian Baroque art at that institution.

Jerome Silbergeld: Jerome Silbergeld, (B.A Stanford University, 1966, M.A. Stanford, 1967, M.A. Univ. of Oregon 1972, Ph.D. Stanford 1974) is the P.Y. and Kinmay W. Tang Professor (Emeritus) of Chinese Art History at Princeton University and director of Princeton’s Tang Center for East Asian Art.  He was formerly the chair of Art History and director of the School of Art and the University of Washington in Seattle, where he taught for twenty-five years.  His research includes traditional and modern Chinese painting, cinema, and architecture and gardens.  Among his book publications are "Chinese Painting Style" (1982); "Mind Landscapes: The Paintings of C. C. Wang" (1987); "Contradictions: Artistic Life, the Socialist State, and the Chinese Painter Li Huasheng" (1993); "China Into Film: Frames of Reference in Contemporary Chinese Cinema" (1999); "Hitchock with a Chinese Face" (2004); "Body in Question: Image and Illusion in Two Chinese Films by Director Jiang Wen" (2008); "Outside In: Chinese x American x Contemporary x Art" (2009); and "Humanism in China: A Contemporary Record of Photography" (2009); among his edited and co-edited publications is "Bridges to Heaven: Essays in East Asian Art in Honor of Wen C. Fong" (2 volumes, 2011).  He has also published more than sixty articles, encyclopedia entries, and book reviews and co-authored the Encyclopædia Britannica entry on Chinese art.

Josef Neuwirth: From 1875 to 1878, he studied history, classical philology, art history and archaeology at the German University in Prague.  In 1882 he obtained his doctorate in art history, becoming an associate professor at Prague in 1894.  In 1897 he attained a full professorship, relocating to Vienna two years later, where he was a professor of art history with special attention to architecture at the Vienna University of Technology.  In 1903–05 he was university rector and in 1920–25, he served as dean to the faculty of architecture.

Question: Jessica Warner's book "John the Painter: Terrorist of the American Revolution" garnered praise from which University Professor of History and Art History at Columbia University?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_praised_book": {
      "type": "string",
      "description": "The name of the person who praised the book."
    },
    "person_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The academic title of the person."
        },
        "university": {
          "type": "string",
          "description": "The university affiliation of the person."
        }
      },
      "required": [
        "title",
        "university"
      ],
      "additionalProperties": false
    },
    "book_title": {
      "type": "string",
      "description": "The title of the book that received praise."
    },
    "author_of_book": {
      "type": "string",
      "description": "The author of the praised book."
    }
  },
  "required": [
    "person_praised_book",
    "person_details",
    "book_title",
    "author_of_book"
  ],
  "additionalProperties": false
}
