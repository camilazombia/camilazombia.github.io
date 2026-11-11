# AI-assisted PQRS

## Summary

An AI-assisted PQRS management experience designed for a high volume of requests. The proposal organizes priorities and recommendations while leaving each change under human control.

## Role and team

My contribution focused on reviewing suggestions, changing individual fields, and composing dynamic emails. Team composition and implementation stages are not documented.

## Context and problem

Request volume created a challenge for reading, classification, and assignment. Introducing AI called for an experience where people could examine recommendations before applying them, rather than treating an automated classification as final.

## Process

I organized the experience around the described tasks: prioritize, understand a request, review its classification, and assign responsibility. The design connected recommendations with field-level controls and a combined action. Model training, accuracy testing, and impact validation are not claimed.

## Key design decisions

- Present a summary to support reading without treating it as a replacement for the original request.
- Separate case type, subtype, department, and assignee for focused review.
- Offer Change for every field to retain human control.
- Make Apply all suggested changes an explicit user action.
- Treat transparency and reversibility as design criteria whose implementation still needs verification.

## Solution

AI prioritizes requests, summarizes them, and recommends classification and assignment. People can change each field or apply the suggestions together. The sending module uses dynamic email and smart tokens to compose messages. Confirmation states and change persistence need to be checked against the implementation.

## Outcomes and learnings

The deliverable is an assisted management proposal that connects recommendations with review controls and email composition. Accuracy, workload, and response-time measurements are not available. The takeaway is that a useful recommendation must also be understandable and correctable.

[DATO PENDIENTE: PQ-01 | evidence of reversal behavior and recommendation evaluation].

## Closing

AI suggests; a person decides. This principle guides how recommendations and controls are presented without claiming autonomous decision-making.
