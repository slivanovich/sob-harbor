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
Institute of Thomas Paine Studies: The Institute for Thomas Paine Studies, or ITPS, is an academic center dedicated to the preservation, study and dissemination of the life, work and legacy of Thomas Paine, and is located on the campus of Iona College in the city of New Rochelle in Westchester County, New York.  Thomas Paine was one of the founding fathers of the United States and the key political philosopher of the age of democratic revolutions.  He was a resident of New Rochelle and lived on a farm just a short distance up North Avenue from the Iona College campus.

Thomas Paine: Thomas Paine (or Pain; February 9, 1737 [O.S. January 29, 1736] – June 8, 1809) was an English-American political activist, philosopher, political theorist, and revolutionary.  One of the Founding Fathers of the United States, he authored the two most influential pamphlets at the start of the American Revolution, and he inspired the rebels in 1776 to declare independence from Britain.  His ideas reflected Enlightenment-era rhetoric of transnational human rights.  He has been called "a corsetmaker by trade, a journalist by profession, and a propagandist by inclination."

A New World: A Life of Thomas Paine: A New World: A Life of Thomas Paine is a 2009 biographical play by the English playwright Trevor Griffiths on the life of Thomas Paine.  Other characters in it include Benjamin Franklin (who appears both as the historical figure and as a narrator), George Washington, Edmund Burke, John Adams and Georges Danton.  Its first half tells of Paine's involvement in the American Revolution and its second half of his involvement in the French Revolution, ending with his funeral.

A Treatise of Human Nature: A Treatise of Human Nature (1738–40) is a book by Scottish philosopher David Hume, considered by many to be Hume's most important work and one of the most influential works in the history of philosophy.  The "Treatise" is a classic statement of philosophical empiricism, skepticism, and naturalism.  In the introduction Hume presents the idea of placing all science and philosophy on a novel foundation: namely, an empirical investigation into human nature.  Impressed by Isaac Newton's achievements in the physical sciences, Hume sought to introduce the same experimental method of reasoning into the study of human psychology, with the aim of discovering the "extent and force of human understanding".  Against the philosophical rationalists, Hume argues that passion rather than reason governs human behaviour.  He introduces the famous problem of induction, arguing that inductive reasoning and our beliefs regarding cause and effect cannot be justified by reason; instead, our faith in induction and causation is the result of mental habit and custom.  Hume defends a sentimentalist account of morality, arguing that ethics is based on sentiment and passion rather than reason, and famously declaring that "reason is, and ought only to be the slave to the passions".  Hume also offers a skeptical theory of personal identity and a compatibilist account of free will.

Common Sense (pamphlet): Common Sense is a pamphlet written by Thomas Paine in 1775–76 advocating independence from Great Britain to people in the Thirteen Colonies.  Written in clear and persuasive prose, Paine marshaled moral and political arguments to encourage common people in the Colonies to fight for egalitarian government.  It was published anonymously on January 10, 1776, at the beginning of the American Revolution, and became an immediate sensation.

Thomas Paine (disambiguation): Thomas Paine (1737–1809) was an English-American political activist, philosopher, political theorist, and revolutionary

God in the Age of Science?: God in the Age of Science? : A Critique of Religious Reason is a 2012 book by the Dutch philosopher Herman Philipse, written in English and published in the United Kingdom.  Philipse found his "Atheist Manifesto" (1995) to be too hastily and superficially written, and decided to set up a more complete work to systematically refute all the arguments for the existence of God epistemologically and to settle accounts with any reason to adhere to any form of theism.

Robert Treat Paine Jr.: Robert Treat Paine Jr. (December 9, 1773 – November 13, 1811) was an American poet and editor.  He was the second son of Robert Treat Paine, signer of the Declaration of Independence.  Born Thomas Paine (after his paternal grandfather), he changed his name to that of his recently deceased older brother in 1801, in part as a tribute to his father and in part to avoid confusion with the more famous Thomas Paine, the revolutionary pamphleteer, who was unpopular at that time.  He received bachelor's and master's degrees from Harvard University, for whose commencement ceremonies he wrote a number of pieces.

The Age of Reason: The Age of Reason; Being an Investigation of True and Fabulous Theology is a work by English and American political activist Thomas Paine, arguing for the philosophical position of Deism.  It follows in the tradition of eighteenth-century British deism, and challenges institutionalized religion and the legitimacy of the Bible.  It was published in three parts in 1794, 1795, and 1807.  It was a best-seller in the United States, where it caused a short-lived deistic revival.  British audiences, however, fearing increased political radicalism as a result of the French Revolution, received it with more hostility.  "The Age of Reason" presents common deistic arguments; for example, it highlights what Paine saw as corruption of the Christian Church and criticizes its efforts to acquire political power.  Paine advocates reason in the place of revelation, leading him to reject miracles and to view the Bible as "an ordinary piece of literature rather than as a divinely inspired text".  It promotes natural religion and argues for the existence of a creator-God.

Joseph L. Lewis: Joseph Lewis (June 11, 1889 – November 4, 1968) was an American freethinker and atheist activist, publisher, and litigator.  During the mid-twentieth century, he was one of America’s most conspicuous public atheists, the other being Emanuel Haldeman-Julius.  Born in Montgomery, Alabama to a Jewish family, he was forced by poverty to leave school at the age of nine to find employment.  He read avidly, becoming self-educated.  Lewis developed his ideas from reading, among others, Robert G. Ingersoll, whose published works made him aware of Thomas Paine.  He later credited Paine's "The Age of Reason" with helping him leave theism.

Question: Joseph L. Lewis (June 11, 1889 – November 4, 1968) was an American freethinker and atheist activist, publisher, and litigator, he later credited Paine's "The Age of Reason" with helping him leave theism, the Age of Reason; Being an Investigation of True and Fabulous Theology is a work by English and American political activist Thomas Paine, arguing for the philosophical position of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "work_name": {
      "type": "string",
      "description": "The common name of the work."
    },
    "work_full_title": {
      "type": "string",
      "description": "The full title of the work, including its subtitle."
    },
    "author_name": {
      "type": "string",
      "description": "The name of the author of the work."
    },
    "philosophical_position_argued": {
      "type": "string",
      "description": "The philosophical position that the work argues for."
    }
  },
  "required": [
    "work_name",
    "work_full_title",
    "author_name",
    "philosophical_position_argued"
  ],
  "additionalProperties": false
}
