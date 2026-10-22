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
Donald Richberg: Donald Randall Richberg (July 10, 1881 - November 27, 1960) was an American attorney, civil servant, and author who was one of President Franklin D. Roosevelt's key aides and who played a critical role in the New Deal.  He co-wrote the National Industrial Recovery Act, was general counsel and executive director of the National Recovery Administration.  He also co-authored the Railway Labor Act, the Norris-LaGuardia Act, and the Taft-Hartley Act.

Railroad Labor Board: The Railroad Labor Board (RLB) was an institution established in the United States of America by the Transportation Act of 1920.  This nine-member panel was designed as means of settling wage disputes between railway companies and their employees.  The Railroad Labor Board's approval of wage reductions for railroad shopmen was instrumental in triggering the Great Railroad Strike of 1922.  The Board was terminated on May 20, 1926 when President Calvin Coolidge signed a new Railway Labor Act into law.

Calvin Coolidge: John Calvin Coolidge Jr. ( ; July 4, 1872 – January 5, 1933) was the 30th President of the United States (1923–29).  A Republican lawyer from Vermont, Coolidge worked his way up the ladder of Massachusetts state politics, eventually becoming governor of that state.  His response to the Boston Police Strike of 1919 thrust him into the national spotlight and gave him a reputation as a man of decisive action.  Soon after, he was elected as the 29th vice president in 1920 and succeeded to the presidency upon the sudden death of Warren G. Harding in 1923.  Elected in his own right in 1924, he gained a reputation as a small-government conservative, and also as a man who said very little, although having a rather dry sense of humor.

Duty of fair representation: The duty of fair representation is incumbent upon U.S. labor unions that are the exclusive bargaining representative of workers in a particular group.  It is the obligation to represent all employees fairly, in good faith, and without discrimination.  Originally recognized by the United States Supreme Court in a series of cases in the mid-1940s involving racial discrimination by railway workers' unions covered by the Railway Labor Act, the duty of fair representation also applies to workers covered by the National Labor Relations Act and, depending on the terms of the statute, to public sector workers covered by state and local laws regulating labor relations.

Aircraft Mechanics Fraternal Association: The Aircraft Mechanics Fraternal Association (AMFA) is an independent craft union representing aircraft maintenance technicians and related employees (ground equipment technicians, maintenance controllers, plant maintenance technicians, facilities maintenance technicians, appearance technicians, maintenance instructors) in the United States.  AMFA is committed to the principles of craft unionism.  It only seeks to represent aircraft maintenance technicians and related employees, a "craft or class" recognized by the National Mediation Board under the Railway Labor Act applied to airlines.  It believes that three characteristics in particular separate AMFA from all other unions: first, direct member control over their local and the finances of it; second, a democratic process where officers are elected instead of appointed, and those same officers can be recalled by the membership; and third, open negotiations where members are invited to attend and participate in collective bargaining sessions.  These three things allow the AMFA membership to effectively maintain control over their union.

Luoyang–Zhanjiang Railway: The Luoyang–Zhanjiang Railway or Luozhan Railway (), is a major rail corridor in China between Luoyang, Henan Province on the Yellow River in the Central Plain, and Zhanjiang, Guangdong Province on the South China Sea.  The rail corridor runs through four provinces and one autonomous region—Henan, Hubei, Hunan, Guangxi and Guangdong—and is designed to facilitate the shipment of goods from the Chinese interior to the Port of Zhanjiang.  The rail corridor was proposed in 1999 and is a combination of preexisting railways and new railway sections built for the Luozhan Railway.  The new railway sections fill a gap in the railway network of South Central China between the Beijing-Guangzhou and Jiaozuo-Liuzhou Railways.  In eastern Guangxi, the Luozhan Railway forks at the town of Cenxi and follows two routes to Zhanjiang.  The Luoyang-Zhanjiang Rail corridor's total length has been reported as 1991 km to 2063.9 km .

National Labor Relations Act of 1935: The National Labor Relations Act of 1935 (49 Stat.  449) (also known as the Wagner Act after New York Senator Robert F. Wagner) is a foundational statute of United States labor law which guarantees basic rights of private sector employees to organize into trade unions, engage in collective bargaining for better terms and conditions at work, and take collective action including strike if necessary.  The act also created the National Labor Relations Board, which conducts elections that can require employers to engage in collective bargaining with labor unions (also known as trade unions).  The Act does not apply to workers who are covered by the Railway Labor Act, agricultural employees, domestic employees, supervisors, federal, state or local government workers, independent contractors and some close relatives of individual employers.

List of airline bankruptcies in the United States: A number of major airlines have declared bankruptcy and have either ceased operations, or reorganized under bankruptcy protection.  Airlines, like any business, are susceptible to market fluctuations and economic difficulties.  The economic structure of the airline industry may contribute to airline bankruptcies as well.  One major element in almost every airline bankruptcy is the rejection by the debtor of its current collective bargaining agreements with employees.  After satisfying certain requirements, bankruptcy law permits courts to approve rejection of labor contracts by the debtor-employer.  With this tool, airline managers reduce costs.  Terms of an employee contract negotiated over years can be eliminated in months through Chapter 11.  Terms of the Railway Labor Act, amended in 1936 to cover airlines, prevent most labor union work actions before, during and after an airline bankruptcy.

Railway Labor Act: The Railway Labor Act is a United States federal law on US labor law that governs labor relations in the railroad and airline industries.  The Act, passed in 1926 and amended in 1934 and 1936, seeks to substitute bargaining, arbitration and mediation for strikes as a means of resolving labor disputes.  Its provisions were originally enforced under the Board of Mediation, but were later enforced under a National Mediation Board.

Railway Mania: Railway Mania was an instance of speculative frenzy in Britain in the 1840s.  It followed a common pattern: as the price of railway shares increased, more and more money was poured in by speculators until the inevitable collapse.  It reached its zenith in 1846, when no fewer than 272 Acts of Parliament were passed, setting up new railway companies, and the proposed routes totalled 9500 mi of new railway.  Around a third of the railways authorised were never built – the companies either collapsed due to poor financial planning, were bought out by larger competitors before they could build their line, or turned out to be fraudulent enterprises to channel investors' money into other businesses.

Question: The president that signed a new Railway Labor Act in 1926 was a lawyer from what state?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "president_name": {
      "type": "string",
      "description": "The name of the president who signed the act."
    },
    "signing_year": {
      "type": "integer",
      "description": "The year the act was signed into law."
    },
    "act_name": {
      "type": "string",
      "description": "The name of the labor act signed."
    },
    "president_origin_state": {
      "type": "string",
      "description": "The state from which the president originated."
    }
  },
  "required": [
    "president_name",
    "signing_year",
    "act_name",
    "president_origin_state"
  ],
  "additionalProperties": false
}
