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
Robert Catesby: Robert Catesby (born in or after 1572, died 8 November 1605) was the leader of a group of provincial English Catholics who planned the failed Gunpowder Plot of 1605.

Thomas Bates: Thomas Bates (1567 – 30 January 1606) was a member of the group of provincial English Catholics who planned the failed Gunpowder Plot of 1605.

Robert Keyes: Robert Keyes was a member of the group of provincial English Catholics who planned the failed Gunpowder Plot of 1605, a conspiracy to assassinate King James I by blowing up the House of Lords during the State Opening of Parliament on 5 November 1605.  He was the sixth man to join the plot.

John Grant (Gunpowder Plot): John Grant (c. 1570 – 30 January 1606) was a member of the failed Gunpowder Plot, a conspiracy to replace the Protestant King James I of England with a Catholic monarch.  Grant was born around 1570, and lived at Norbrook in Warwickshire.  He married the sister of another plotter, Thomas Wintour.  Grant was enlisted by Robert Catesby, a religious zealot who had grown so impatient with James's lack of toleration for Catholics that he planned to kill him, by blowing up the House of Lords with gunpowder.  Grant's role in the conspiracy was to provide supplies for a planned Midlands uprising, during which James's daughter, Princess Elizabeth, would be captured.  However, on the eve of the planned explosion, Guy Fawkes was discovered guarding the explosives the plotters had positioned in the undercroft beneath the House of Lords, and arrested.

John and Christopher Wright: John (Jack) Wright (January 1568 – 8 November 1605), and Christopher (Kit) Wright (1570?  – 8 November 1605), were members of the group of provincial English Catholics who planned the failed Gunpowder Plot of 1605, a conspiracy to assassinate King James I by blowing up the House of Lords.  Their sister married another plotter, Thomas Percy.  Educated at the same school in York, the Wrights had early links with Guy Fawkes, the man left in charge of the explosives stored in the undercroft beneath the House of Lords.  As known recusants the brothers were on several occasions arrested for reasons of national security.  Both were also members of the Earl of Essex's rebellion of 1601.

Gunpowder Plot: The Gunpowder Plot of 1605, in earlier centuries often called the Gunpowder Treason Plot or the Jesuit Treason, was a failed assassination attempt against King James I of England and VI of Scotland by a group of provincial English Catholics led by Robert Catesby.

Guy Fawkes: Guy Fawkes ( ; 13 April 1570 – 31 January 1606), also known as Guido Fawkes, the name he adopted while fighting for the Spanish, was a member of a group of provincial English Catholics who planned the failed Gunpowder Plot of 1605.

Thomas Percy (Gunpowder Plot): Thomas Percy (  1560 – 8 November 1605) was a member of the group of provincial English Catholics who planned the failed Gunpowder Plot of 1605.  A tall, physically impressive man, little is known of his early life beyond his matriculation in 1579 at the University of Cambridge, and his marriage in 1591 to Martha Wright.  In 1596 his second cousin once removed, Henry Percy, 9th Earl of Northumberland, appointed him constable of Alnwick Castle and made him responsible for the Percy family's northern estates.  He served the earl in the Low Countries in about 1600–1601, and in the years before 1603 was his intermediary in a series of confidential communications with King James VI of Scotland.

Everard Digby: Sir Everard Digby (c. 1578 – 30 January 1606) was a member of the group of provincial English Catholics who planned the failed Gunpowder Plot of 1605.  Although he was raised in a Protestant household, and married a Protestant, Digby and his wife were converted to Catholicism by the Jesuit priest John Gerard.  In the autumn of 1605 he was part of a Catholic pilgrimage to the shrine of St Winefride's Well in Holywell.  About this time he met Robert Catesby, a religious fanatic who planned to blow up the House of Lords with gunpowder, killing James I.  Catesby then planned to incite a popular revolt, during which a Catholic monarch would be restored to the English throne.

Gunpowder Plot in popular culture: The Gunpowder Plot was a failed assassination attempt against King James VI of Scotland and I of England by a group of provincial English Catholics led by Robert Catesby.  The conspirators' aim was to blow up the House of Lords at the State Opening of Parliament on 5 November 1605, while the king and many other important members of the aristocracy and nobility were inside.  The conspirator who became most closely associated with the plot in the popular imagination was Guy Fawkes, who had been assigned the task of lighting the fuse to the explosives.

Question: The Gunpowder Plot was a failed assassination attempt against King James VI of Scotland and I of England by a group of provincial English Catholics led by Robert Catesby, was the leader of a group of provincial English Catholics who planned the failed Gunpowder Plot of which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "plot_name": {
      "type": "string",
      "description": "The name of the historical plot."
    },
    "plot_year": {
      "type": "integer",
      "description": "The year the plot was planned or occurred."
    },
    "plot_leader": {
      "type": "string",
      "description": "The name of the leader of the plot."
    },
    "plot_target": {
      "type": "string",
      "description": "The primary target of the assassination attempt."
    },
    "plot_outcome": {
      "type": "string",
      "description": "The outcome of the plot (e.g., 'failed', 'successful')."
    }
  },
  "required": [
    "plot_name",
    "plot_year",
    "plot_leader",
    "plot_target",
    "plot_outcome"
  ],
  "additionalProperties": false
}
