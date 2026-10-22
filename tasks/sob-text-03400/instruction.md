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
Miracles Ain't What They Used To Be: Miracles Ain't What They Used To Be Plus... is a 2016 collection of memoirs and essays by American author Joe R. Lansdale.  It includes Lansdale's essays on how he came to be an author, and on his inspirations, personal beliefs, ideas for the vast amount of published work he has done over his 40 years of writing novels, short stories, novellas, and comic books.  This book shows a never before insight into his long career.  This is the first book in which Lansdale discusses his ideas and personal beliefs that influence his storytelling which has spanned 40 years and has included over 40 novels and almost as many short story collections.  It is a rare glimpse into the mind that has entertained so many readers over the years.  His work has been adapted to several films and most recently into a series on The Sundance Channel with his first bringing of longtime protagonist Hap and Leonard to television.  Season 2 is now filming.

Anna Bowman Dodd: Anna Bowman Dodd (née Blake; January 21, 1858 - January 1929) was a 19th-century author from New York.  She wrote short stories, essays and a series of articles on church music.  After Dodd wrote a paper on the Concord School of Philosophy for "Appleton's Magazine", English journals copied it, a French translation was reprinted in Émile Littré's "Revue Philosophique", and the author found her services in growing demand.  She was engaged by "Harper's Magazine" in 1881 to furnish an exhaustive article on the political leaders of France, which she prepared for by going to France, in order to study the subject more closely.  The paper's editor, Henry Mills Alden, pronounced it as 'the most brilliant article of the kind we have had in ten years'.  Before returning to the U.S., she visited Rome and prepared a description of the carnival for "Harper's".

L. Ron Hubbard: Lafayette Ronald Hubbard (March 13, 1911 – January 24, 1986), better known as L. Ron Hubbard ( ) and often referred to by his initials, LRH, was an American author and the founder of the Church of Scientology.  After establishing a career as a writer, becoming best known for his science fiction and fantasy stories, he developed a system called Dianetics which was first expounded in book form in May 1950.  He subsequently developed his ideas into a wide-ranging set of doctrines and practices as part of a new religious movement that he called Scientology.  His writings became the guiding texts for the Church of Scientology and a number of affiliated organizations that address such diverse topics as business administration, literacy and drug rehabilitation.  The Church's dissemination of these materials led to Hubbard being listed by the "Guinness Book of World Records" as the most translated and published author in the world.  The Guinness World Record for the most audio books published for one author is also held by Hubbard.  In 2014, Hubbard was cited by "Smithsonian" magazine as one of the 100 most significant Americans of all time, as one of the eleven religious figures on that list.

Church of Christ (Restored): The Church of Christ (Restored) is a denomination within the Latter Day Saint movement that split from the Church of Christ (Fettingite) in the late 1930s under the leadership of Elder A. C. DeWolf.  This schism was provoked by a difference in opinion regarding a series of claimed "messages" received by William Draves, an elder in that church, following the death of founder Otto Fetting.  Whereas the main Fettingite church initially chose to grant cautious acceptance to these missives, several Fettingite branches in Louisiana and Mississippi did not, and split from the main organization to form the Church of Christ (Restored).  Even after the main Fettingite church chose to reject Draves and his messages in 1943 (leading Draves to leave and found his own sect, the Church of Christ with the Elijah Message), the DeWolf faction refused to reconcile with the main body, considering itself to be the sole legitimate continuation of the Fettingite church, and the only true church on earth today.  Its membership is currently concentrated mostly in the American South, and stands at about 450 members.

Harry Webb Farrington: Harry Webb Farrington (1879–1930) was an American author, poet, hymn writer, preacher, soldier, and educator.  He was an orphan who lived in Baltimore, Maryland, Bel Air, Maryland, and Darlington, Maryland.  He is famous still as being a member of the Darlington United Methodist Church and witnessing the great revivals of the late 1890s.  The story of his life comes from one of his books, "Kilts to Togs: Orphan Adventures" (1930).  He is also the author of "Cher Ami" (1926), "Rough and Brown", "Walls of America" (1925), and "Roosevelt the Righteous" (1925).  He also wrote "Poems from France" in 1920.

History of Dianetics: The history of Dianetics possibly begins in the 1920s.  Its originator L. Ron Hubbard claimed that his ideas of Dianetics originated in the 1920s and 1930s.  By his own account, he spent a great deal of time in the Oak Knoll Naval Hospital's library, where he would have encountered the work of Freud and other psychoanalysts.  In April 1950, Hubbard and several others established the Hubbard Dianetic Research Foundation in Elizabeth, New Jersey to coordinate work related for the forthcoming publication.  Hubbard first introduced Dianetics to the public in the article "" published in the May 1950 issue of the magazine "Astounding Science Fiction".  Hubbard wrote "" at that time, allegedly completing the 180,000-word book in six weeks.

Lloyd Pye: Lloyd Anthony Pye Jr. (September 7, 1946 – December 9, 2013) was an American author and paranormal researcher best known for his promotion of the Starchild skull.  He claimed it was the relic of a human-alien hybrid, although genetic testing showed it to be from a human male.  He also promoted the ideas that cryptozoological creatures such as Bigfoot are real and that aliens intervened in human development.

John M. Barry: John M. Barry (b. 1947) is an American author and historian, perhaps best known for his award-winning books on the Great Mississippi Flood of 1927, the influenza pandemic of 1918, and the development of the modern form of the ideas of separation of church and state and individual liberty.  His most recent book is "Roger Williams and the Creation of the American Soul: Church, State, and the Birth of Liberty" (Viking 2012).  He has also been honored by the National Academies of Science, has served on advisory boards and committees at MIT and Johns Hopkins, is Distinguished Scholar and adjunct faculty at Tulane University, and was subject of a cover story in The New York Times Magazine Oct. 5, 2014, https://www.nytimes.com/interactive/2014/10/02/magazine/mag-oil-lawsuit.html?_r=2

Scientology: Scientology is a body of religious beliefs and practices developed in 1954 by American author L. Ron Hubbard (1911–86).  Hubbard initially developed a program of ideas called Dianetics, which was distributed through the Dianetics Foundation.  The foundation soon entered bankruptcy, and Hubbard lost the rights to his seminal publication "" in 1952.  He then recharacterized the subject as a religion and renamed it Scientology, retaining the terminology, doctrines, the E-meter, and the practice of auditing.  Within a year, he regained the rights to Dianetics and retained both subjects under the umbrella of the Church of Scientology.

Written works of L. Ron Hubbard: Lafayette Ronald Hubbard (March 13, 1911 – January 24, 1986), better known as L. Ron Hubbard, was an American pulp fiction author.  He wrote in a wide variety of genres, including science fiction, fantasy, adventure fiction, aviation, travel, mystery, western and romance.  He is perhaps best known for his self-help book, the #1 New York Times bestseller Dianetics: The Modern Science of Mental Health (first published in 1950), and as the founder of the Church of Scientology.

Question: What type of church did this American author found who claimed the ideas of Dianetics originated in the 1920s and 1930s?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the American author identified by the Dianetics origin claim."
    },
    "author_nationality": {
      "type": "string",
      "description": "The nationality of the author."
    },
    "dianetics_origin_claim_period": {
      "type": "string",
      "description": "The period in which the author claimed the ideas of Dianetics originated."
    },
    "founded_church_name": {
      "type": "string",
      "description": "The name of the church founded by the author."
    },
    "church_type_description": {
      "type": "string",
      "description": "A description of the nature or type of the founded church/movement."
    }
  },
  "required": [
    "author_name",
    "author_nationality",
    "dianetics_origin_claim_period",
    "founded_church_name",
    "church_type_description"
  ],
  "additionalProperties": false
}
