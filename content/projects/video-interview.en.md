# Video Interview

## Summary

A video interview feature requested by Remote Latinos clients. Candidates answer role-specific questions one step at a time, with interview transcription included in the experience.

## Role and team

I worked on the guided flow and the definition of recording states and edge cases. Clients supplied the functional need; the full delivery team is not documented.

## Context and problem

The request was to add video answers to questions related to a candidate’s role. The experience challenge was to guide a sequential activity that depends on recording and must account for errors and retries.

## Process

I organized the question sequence and video response interaction. The design considered recording, error, and retry states, together with edge cases across the journey. There is no candidate testing protocol or validation evidence available to claim.

## Key design decisions

- Present questions step by step to focus attention on the current response.
- Connect questions with the role to retain interview context.
- Distinguish recording, error, and retry states to communicate task status.
- Include transcription as part of the requested feature to support video review.

## Solution

The proposal combines role-specific questions, sequential video responses, and transcription. Recording and recovery states are part of the design narrative. Exact rules for duration, camera permissions, interruptions, and saving need confirmation from product specifications and are not invented here.

## Outcomes and learnings

The documented output is a guided interview feature design with recording states. Completion, error, and usage data are not available. The takeaway is that designing a recording experience also means defining how people understand and recover from a failed attempt.

[DATO PENDIENTE: VI-01 | approved matrix of recording states, recovery behavior, and limits].

## Closing

The case focuses on supporting a demanding task with understandable steps and states, without claiming unmeasured hiring improvements.
