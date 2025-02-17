# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start'successor successors:", problem.getSuccessors(problem.getStartState())
    """
    #applying Depth first search strategy on search tree using stack as fringe
    start_state=problem.getStartState()
    fringe=util.Stack()
    fringe.push((start_state,{"directions":[]}))
    is_goal_reached=0
    visited=[]
    directions=[]
    while(not fringe.isEmpty()):
        current_node=fringe.pop()
        if (current_node[0] not in visited):
            visited.append(current_node[0])
            if (problem.isGoalState(current_node[0])):
                # break if the current state is the goal state
                is_goal_reached = 1
                break
            else:
                # else iterate through all the successors and add unvisited nodes to fringe
                successors = []
                successors = problem.getSuccessors(current_node[0])
                for successor in successors:
                    if (successor[0] not in visited):
                        par_directions = copy.deepcopy(current_node[1]['directions'])
                        fringe.push((successor[0], {"directions": par_directions + [successor[1]]}))

    directions=current_node[1]["directions"]
    if(is_goal_reached==1):
        return directions
    else:
        # we have not reached goal state
        return []
    
  

def breadthFirstSearch(problem):
    '''
        applying Depth first search strategy on search tree using queue as fringe
    '''
    start_state=problem.getStartState()
    fringe=util.Queue()
    fringe.push((start_state,{"directions":[]}))
    is_goal_reached=0
    visited=[]
    directions=[]
    while(not fringe.isEmpty()):
        current_node=fringe.pop()
        if(current_node[0] not in visited):
            visited.append(current_node[0])

            if(problem.isGoalState(current_node[0])):
                #goal state is reached
                is_goal_reached=1
                break
            else:
                successors=[]
                successors=problem.getSuccessors(current_node[0])
                for successor in successors:
                    if(successor[0] not in visited):
                        par_directions=copy.deepcopy(current_node[1]['directions'])
                        fringe.push((successor[0],{"directions":par_directions+[successor[1]]}))
            
                
    directions=current_node[1]["directions"]
    #print sol
    if(is_goal_reached==1):
        return directions
    else:
        return []
    

def uniformCostSearch(problem):
    '''
        gets the optimal cost but explores in all possible directions uniformly on the cost
        using priority
    '''
    start_state=problem.getStartState()
    fringe=util.PriorityQueue()
    fringe.push((start_state,{"directions":[]}),0)
    is_goal_reached=0
    visited=[]
    directions=[]
    while(not fringe.isEmpty()):
       
        current_node=fringe.pop()
        if(current_node[0] not in visited):
            visited.append(current_node[0])
            # print "current",curr
            if (problem.isGoalState(current_node[0])):
                is_goal_reached = 1
                break
            else:
                successors = []
                successors = problem.getSuccessors(current_node[0])
                for successor in successors:
                    if (successor[0] not in visited):
                        par_directions = copy.deepcopy(current_node[1]['directions'])
                        dirs = par_directions + [successor[1]]
                        #cost to reach the goal
                        cost = problem.getCostOfActions(dirs)
                        fringe.push((successor[0], {"directions": par_directions + [successor[1]]}), cost)

    directions=current_node[1]["directions"]
    if(is_goal_reached==1):
        return directions
    else:
        return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    '''
        performs astar search on the search tree using the heuristics
        using priority queue
    '''
    start_state=problem.getStartState()
    fringe=util.PriorityQueue()
    fringe.push((start_state,{"directions":[]}),0)
    is_goal_reached=0
    visited=[]
    directions=[]
    while(not fringe.isEmpty()):
       
        current_state=fringe.pop()
        if (current_state[0] not in visited):
            visited.append(current_state[0])
            if (problem.isGoalState(current_state[0])):
                is_goal_reached = 1
                break
            else:
                successors = []
                successors = problem.getSuccessors(current_state[0])
                for directions in successors:
                    #push only the unvisited successors
                    if (directions[0] not in visited):
                        par_directions = copy.deepcopy(current_state[1]['directions'])
                        dirs = par_directions + [directions[1]]
                        # cost = cost of path + heuristic cost
                        cost = problem.getCostOfActions(dirs) + heuristic(directions[0], problem)
                        fringe.push((directions[0], {"directions": par_directions + [directions[1]]}), cost)

    directions=current_state[1]["directions"]
    if(is_goal_reached==1):
        return directions
    else:
        return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

