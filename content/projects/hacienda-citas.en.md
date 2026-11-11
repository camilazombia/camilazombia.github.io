# Appointment scheduling

## Summary

A scheduling platform design for Hacienda. The proposal connects appointment requests with schedule management and distinguishes the responsibilities of administrators, coordinators, and agents.

## Role and team

I worked on flows, interfaces, and system behavior definitions, including scheduling rules and permissions by role. A complete team breakdown is not available.

## Context and problem

The process was fragmented: an Excel file was sent to a provider to enable availability, the request form had usability issues, and a separate Teams calendar lacked detail. This separation made it difficult to understand the service from configuration through appointment handling.

## Process

Using the described existing workflows, I defined a platform structure with role-based management and a request form. The design work specified rules, limits, and dynamic schedule behavior. User testing, deployment, and operational outcomes are not claimed without supporting evidence.

## Key design decisions

- Distinguish administrators, coordinators, and agents to clarify responsibility.
- Give the administrator overall control, including email, to configure the service.
- Provide coordinators with an office-specific dashboard to keep management grounded in their operation.
- Design dynamic schedules where adding a block adjusts the others to account for the whole schedule.
- Define request limits as system rules so the form does not rely on implicit decisions.

## Solution

The proposal includes an appointment request form, an administrator profile controlling email and scheduling rules, and an office dashboard where coordinators create dynamic schedules. The agent is part of the role model; detailed permissions still need confirmation.

## Outcomes and learnings

Previously, the workflow relied on provider-bound files, a form, and a separate calendar. The design brings those needs into a platform proposal with defined roles and scheduling behavior. This is a design deliverable, not a confirmed deployment or measured time saving. The main takeaway is to treat rules and permissions as a core part of the experience.

[DATO PENDIENTE: HC-01 | confirmation of agent permissions and implementation status].

## Closing

The case makes service logic visible to both the people managing appointments and those requesting them. Visual examples will use fictional information.
