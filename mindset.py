##########################################################################################################################################################
# think as a manager:
##########################################################################################################################################################
## what is the goal
## what is the process

### what kind of people do you need to hire to get this done ==> people == agents 
### which processes and tasks do I Expect them to do
## what are the roles of the agents, the backstory, the goal 
## be specific : 
### writer != senior copywriter writer
### Researcher != HR research specialist
### Financial analyst != FINRA analyst
##########################################################################################################################################################

##########################################################################################################################################################
# Step by step guide:
##########################################################################################################################################################
# 1. Import the necessary classes from the crewai module.
# 2. Create a new agent using the Agent class.
# 3. Define the role, goal, and backstory for the agent.
# 4. Create a new task using the Task class.
# 5. Define the description, expected output, and agent for the task.
# 6. Create a new crew using the Crew class.
# 7. Add the agents and tasks to the crew.
# 8. Run the crew by calling the kickoff method with the inputs.
# 9. Print the result of the crew execution.
##########################################################################################################################################################

##########################################################################################################################################################
# Key elements of AI agents:
##########################################################################################################################################################
# 1. Role: The role of the agent in the crew. (Roles, Goals, Backstory)
# 2. Focus: The primary focus or goal of the agent. (Tasks, Objectives)
# 3. Tools: The tools or resources available to the agent. 
# 4. Cooperation: The level of cooperation with other agents. (feedback, delegation)
# 5. Guardrails: The constraints or limitations on the agent's actions. 
# 6. Memory: The memory or history of the agent's interactions.
## short term memory: memory during excution of a task, share knowledge with other agents, share intermediate info even before task completion
## long term memory: stored in local database, used for future tasks, leads to self improvement of agents
## entity memory: also short term
##########################################################################################################################################################

##########################################################################################################################################################
#Tools:
##########################################################################################################################################################
## Versatile
## Caching
## Fault Tolerant
##########################################################################################################################################################

##########################################################################################################################################################
#Tasks:
##########################################################################################################################################################
## clear description of the task
## clear and concise expected output
##########################################################################################################################################################

##########################################################################################################################################################
# Agents collaboration
##########################################################################################################################################################
# sequential agent: - initial info will fade out as we move forward
# Hierarchical agent: - agent manager / agents executor
# Parallel agent: - agents working in parallel
# Collaborative agent: - agents working together
##########################################################################################################################################################