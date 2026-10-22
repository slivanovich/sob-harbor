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
James Madison College: James Madison College is a college of public affairs and international relations within Michigan State University in East Lansing, Michigan, USA.  It was founded in 1967, "with a vision of creating a residential college merging the best attributes of a small college with an undergraduate education focusing on public affairs and firmly rooted in liberal arts"; the college was named after James Madison in honor of his role in writing the United States Constitution, the Bill of Rights, and "The Federalist Papers" (which form part of the College's core curriculum).  Originally considered experimental, the college has since come to be recognized as among the best in the nation.

Penn State University Press: Penn State University Press, also called The Pennsylvania State University Press, was established in 1956, and is a non-profit publisher of scholarly books and journals.  It is the independent publishing branch of the Pennsylvania State University and is a division of the Penn State University Library system.  The Penn State University Press primarily publishes scholarship but, as a part of a land-grant university with a mandate to serve the citizens of the commonwealth of Pennsylvania, it also specializes in producing books about Pennsylvania and the Penn State University.  The areas of scholarship the Press is most known for are philosophy, art history, medieval studies, Latin American studies, political science, religious studies, and early American history.  The Penn State Press employs approximately 24 people, and produces about 70 books a year and over 50 journals.  The Press also has several internship programs for Penn State students interested in a publishing career.

Peter G. Klein: Peter G. Klein is an American Austrian School economist who studies managerial and organizational issues.  Klein is professor of entrepreneurship at Baylor University’s Hankamer School of Business and senior research fellow at the Baugh Center for Entrepreneurship and Free Enterprise.  He came to Baylor from the University of Missouri, where he was professor of applied social sciences and professor of public affairs.  Klein is also adjunct professor of strategy and management at the Norwegian School of Economics and Business Administration and Carl Menger Research Fellow at the Mises Institute.  He serves as field editor for the "Journal of Business Venturing", associate editor of the "Academy of Management Perspectives", and associate editor of "The Independent Review".  His 2012 book "Organizing Entrepreneurial Judgment" (with Nicolai Foss, Cambridge University Press) won the 2014 Foundation for Economic Education Best Book Prize, and his 2010 book "The Capitalist and the Entrepreneur" (Mises Institute) has been translated into Chinese and Portuguese.  He holds an honorary professorship at the Beijing University of Information Science and Technology.

Education Review: Education Review (ISSN 1094-5296  ) is an open-access academic journal publishing reviews of books in the field of education.  It was established in 1998 by Gene V. Glass, Nicholas Burbules (University of Illinois at Urbana–Champaign), and Kate Corby (Michigan State University).  The journal publishes peer-reviewed essay reviews and reviews of scholarly books.  Reviews of books published in Spanish and Portuguese are also published.  Reviews in English were edited by Glass (from 1998 to 2012) and co-editor Melissa Cast-Brede (University of Nebraska at Omaha).  They were succeeded in 2012 by David J. Blacker (University of Delaware).  Reviews in Spanish or Portuguese are edited by Gustavo Fischman (Arizona State University).  "Education Review" publishes approximately 250 reviews each year.  Starting in 2010, "Education Review" was published by the National Education Policy Center at the School of Education, University of Colorado at Boulder.

Asian Journal of Public Affairs: The Asian Journal of Public Affairs is a biannual academic journal covering public affairs issues pertaining to Asia and the Oceania region.  It is edited by graduate students from the Lee Kuan Yew School of Public Policy at the National University of Singapore.  The journal's scope includes, but is not limited to, public policy, public management, international relations, international political economy, and economics.  Each issue features scholarly submissions, case studies, book reviews, and commentaries.

John Glenn College of Public Affairs: The John Glenn College of Public Affairs is a public policy and management school at The Ohio State University.  The Glenn College offers undergraduate, graduate and doctoral programs in public affairs.  The Glenn College provides research, training and technical assistance to state, public and nonprofit organizations.  The college is named after United States Senator and Astronaut John Glenn.  On January 30, 2015, the Ohio State University Board of Trustees approved a change of status of the former John Glenn School of Public Affairs making the new John Glenn College of Public Affairs the 15th college at The Ohio State University.

Michigan State University Press: Michigan State University Press is the scholarly publishing arm of Michigan State University, the nation’s pioneer land-grant university (the institution that served as the prototype for schools established under the Morrill Land-Grant Acts of 1862).  Although a formal press was not established at MSU until the middle of the 20th century, scholarly publishing was an important part of the institution’s mission from early on; scholarly publishing at Michigan State significantly predates the establishment of its press.  By the 1890s the institution’s Experiment Stations began issuing a broad range of influential publications in the natural sciences (including a beautifully illustrated Birds of Michigan in 1892) and as early as 1876, professor A.J. Cook commissioned a Lansing printer to issue his popular Manual of the Apiary, which ran through numerous editions and remained in print for nearly half a century.

Darwinism, Design and Public Education: Darwinism, Design and Public Education is a 2003 anthology, consisting largely of rewritten versions of essays from a 1998 issue of Michigan State University Press's journal, "Rhetoric and Public Affairs", edited by intelligent design activists John Angus Campbell (who serves on the journal's editorial board) and Stephen C. Meyer, neither of whom are scientists.  The book is promoted as being a "peer-reviewed science book", however in reviewing it Barbara Forrest notes that:

Barbara Forrest: Barbara Carroll Forrest is a professor of philosophy at Southeastern Louisiana University in Hammond, Louisiana.  She is a critic of intelligent design and the Discovery Institute.

Philosophy &amp; Rhetoric: Philosophy & Rhetoric is a peer-reviewed academic journal covering the relationship between philosophy and rhetoric.  The journal was established in 1968 by Henry Johnstone Jr., who served as its editor-in-chief until 1998.  The editorship then passed to a group of scholars until 2003 when the current editor took over.  The journal is published quarterly by the Penn State University Press.

Question: Darwinism, Design and Public Education, released in which year, is an anthology, consisting largely of rewritten versions of essays from a 1998 issue of Michigan State University Press's journal, "Rhetoric and Public Affairs", the book is promoted as being a "peer-reviewed science book", however in reviewing it Barbara Forrest, stated differently?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "book_title": {
      "type": "string",
      "description": "The title of the book."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the book was released."
    },
    "is_anthology": {
      "type": "boolean",
      "description": "Indicates if the book is an anthology."
    },
    "origin_details": {
      "type": "object",
      "properties": {
        "source_journal": {
          "type": "string",
          "description": "The name of the journal from which essays were largely rewritten."
        },
        "source_journal_issue_year": {
          "type": "integer",
          "description": "The year of the journal issue that served as the source."
        },
        "publishing_press": {
          "type": "string",
          "description": "The press that publishes the source journal."
        }
      },
      "required": [
        "source_journal",
        "source_journal_issue_year",
        "publishing_press"
      ],
      "additionalProperties": false
    },
    "review_details": {
      "type": "object",
      "properties": {
        "promoted_as": {
          "type": "string",
          "description": "How the book was promoted."
        },
        "reviewer_name": {
          "type": "string",
          "description": "The name of the person who reviewed the book."
        },
        "reviewer_stance_summary": {
          "type": "string",
          "description": "A summary of the reviewer's stance regarding the promotion claim."
        }
      },
      "required": [
        "promoted_as",
        "reviewer_name",
        "reviewer_stance_summary"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "book_title",
    "release_year",
    "is_anthology",
    "origin_details",
    "review_details"
  ],
  "additionalProperties": false
}
