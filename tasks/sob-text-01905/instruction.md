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
Francis R. Valeo: Francis Ralph "Frank" Valeo (January 30, 1916 – April 9, 2006) was the Secretary of the United States Senate and "ex officio" member of the Federal Election Commission.  He was the defendant/appellee for the Federal government of the United States in Buckley v. Valeo, 424 U.S. 1 (1976), in which the Supreme Court of the United States upheld federal limits on campaign contributions.

Sackett v. Environmental Protection Agency: Sackett v. United States Environmental Protection Agency, 566 U.S. ___ (2012) , is a United States Supreme Court case in which the Court held that the Clean Water Act is subject to the Administrative Procedure Act, which requires an appeals process for any ruling by a federal agency.  The Court ruled that the availability of immediate judicial review of compliance orders issued by the United States Environmental Protection Agency is required.

Citizens Against Rent Control v. City of Berkeley: Citizens Against Rent Control v. City of Berkeley, 454 U.S. 290 (1981), was a case in which the Supreme Court of the United States invalidated a California law that set limits on contributions to ballot issue campaigns.  The ruling relies heavily on the Court's earlier decisions in Buckley v. Valeo, holding that limits on contributions to political candidates implicate the First Amendment, and First National Bank of Boston v. Bellotti, holding that the state governments have no compelling interest in limiting spending on speech about ballot issues.

Osborne v. Ohio: Osborne v. Ohio, 495 U.S. 103 (1990) , is a U.S. Supreme Court case in which the Court held that the First Amendment allows states to outlaw the mere possession, as distinct from the distribution, of child pornography.  In so doing, the Court extended the holding of "New York v. Ferber", 458 U.S. 747 (1982) , which had upheld laws banning the distribution of child pornography against a similar First Amendment challenge, and distinguished "Stanley v. Georgia", 394 U.S. 557 (1969) , which had struck down a Georgia law forbidding the possession of pornography by adults in their own homes.  The Court also determined that the Ohio law at issue was not overbroad, relying on a narrowing interpretation of the law the Ohio Supreme Court had adopted in prior proceedings in the case.  However, because it was unclear whether the State had proved all the elements of the crime, the Court ordered a new trial.

Miami Herald Publishing Co. v. Tornillo: Miami Herald Publishing Co. v. Tornillo, 418 U.S. 241 (1974), was a United States Supreme Court case that overturned a Florida state law requiring newspapers to allow equal space in their newspapers to political candidates in the case of a political editorial or endorsement content.  The court held that while the statute does not "prevent [newspapers] from saying anything [they] wish" it "exacts a penalty on the basis of the content."  Because newspapers are economically finite enterprises, "editors may conclude that the safe course is to avoid controversy," thereby chilling speech.  Furthermore, the Court held the exercise of editorial judgement is a protected First Amendment activity.  In effect, this ruling reaffirmed the constitutional principle of freedom of the press (detailed in the First Amendment) and prevented state governments from controlling the content of the press.  This case illustrates the medium with the most Constitutional protection—newspapers—while "Red Lion Broadcasting Co. v. FCC" represents the medium with the least protection—broadcast, television, and radio.

Randall v. Sorrell: Randall v. Sorrell, 548 U.S. 230 (2006), is a decision by the Supreme Court of the United States involving a Vermont law which placed a cap on financial donations made to politicians.  The court ruled that Vermont's law, the strictest in the nation, unconstitutionally hindered the citizens' First Amendment right to free speech.  A key issue in the case was the 1976 case "Buckley v. Valeo", which many justices felt needed to be revisited.

United States v. Alvarez: United States v. Alvarez, 567 U.S. 709 (2012) , is a United States Supreme Court case in which the Court struck down the Stolen Valor Act, a federal law that criminalized false statements about having a military medal.  The law had been passed as an effort to stem instances where people falsely claimed to have earned the medal in an attempt to protect the "valor" of those who really had.  While a 6-3 majority of the Supreme Court agreed that the law was unconstitutional under the First Amendment's free speech protections, it could not agree on a single rationale.  Four justices concluded that a statement's falsity is not enough, by itself, to exclude speech from First Amendment protection.  Another two justices concluded that while false statements were entitled to some protection, the Stolen Valor Act was invalid because it could have achieved its objectives in less restrictive ways.

Massachusetts v. Environmental Protection Agency: Massachusetts v. Environmental Protection Agency, 549 U.S. 497 (2007), is a 5-4 U.S. Supreme Court case in which twelve states and several cities of the United States brought suit against the Environmental Protection Agency (EPA) to force that federal agency to regulate carbon dioxide and other greenhouse gases (GHGs) as pollutants.

Buckley v. Valeo: Buckley v. Valeo, 424 US 1 (1976) is a US constitutional law Supreme Court case on campaign finance.  A majority of judges held that limits on election spending in the Federal Election Campaign Act of 1971 §608 are unconstitutional.  In a "per curiam" (by the Court) opinion, they ruled that expenditure limits contravene the First Amendment provision on freedom of speech because a restriction on spending for political communication necessarily reduces the quantity of expression.  It limited disclosure provisions and limited the Federal Election Commission's power.  Justice Byron White dissented in part and wrote that Congress had legitimately recognized unlimited election spending "as a mortal danger against which effective preventive and curative steps must be taken."

Michigan v. EPA: Michigan v. Environmental Protection Agency, 576 U.S. ___ (2015) , was a landmark United States Supreme Court case in which the Court analyzed whether the Environmental Protection Agency must consider costs when deciding to regulate, rather than later in the process of issuing the regulation.  Writing for a 5–4 majority, Justice Antonin Scalia held that the EPA must consider costs and that it interpreted the Clean Air Act unreasonably when it determined that it did not need to consider costs when it issued a "finding" that it was "necessary and appropriate" to regulate.  Critics of the Environmental Protection Agency praised the Court's decision, while other commentators criticized Justice Scalia's decision to ignore health impacts in his opinion.  Some commentators suggested that the decision may derail President Barack Obama's climate change agenda entirely.

Question: Which supreme court case likened political spending to the first amendment, Buckley v. Valeo or Massachusetts v. Environmental Protection Agency?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "supreme_court_case_name": {
      "type": "string",
      "description": "The name of the Supreme Court case that addressed the question."
    },
    "constitutional_amendment_involved": {
      "type": "string",
      "description": "The specific constitutional amendment central to the case's ruling."
    },
    "concept_likened_to_amendment": {
      "type": "string",
      "description": "The concept that the court likened to the constitutional amendment."
    },
    "ruling_summary": {
      "type": "string",
      "description": "A brief summary of the court's ruling regarding the linkage between the concept and the amendment."
    }
  },
  "required": [
    "supreme_court_case_name",
    "constitutional_amendment_involved",
    "concept_likened_to_amendment",
    "ruling_summary"
  ],
  "additionalProperties": false
}
