<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

interface Project {
    id: number,
    tasks: string[],
    name: string,
    completion_percentage: number
}

const FLASK_API_BASE_URL: string = "http://127.0.0.1:5000/api/projects/new";

// Single ref object for all form data
const formData = ref({
    name: '',
    tasksInput: '',
    completion_percentage: 0
});

const submitProject = async () => {
    try {
        // Convert tasksInput (string) to tasks array by splitting on newlines
        const tasks = formData.value.tasksInput
            .split('\n')
            .map(task => task.trim())
            .filter(task => task.length > 0);

        const projectData: Omit<Project, 'id'> = {
            name: formData.value.name,
            tasks: tasks,
            completion_percentage: formData.value.completion_percentage
        };

        const response = await fetch(FLASK_API_BASE_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(projectData)
        });

        if (response.ok) {
            // Reset form after successful submission
            formData.value = {
                name: '',
                tasksInput: '',
                completion_percentage: 0
            };
            alert('Project submitted successfully!');
            router.push('/')
        } else {
            alert('Error submitting project');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error submitting project');
    }
};
</script>

<template>
    <form @submit.prevent="submitProject" class="project-form">
        <div class="form-group">
            <label for="projectName">Project Name:</label>
            <input type="text" id="projectName" v-model="formData.name" required placeholder="Enter project name"
                class="form-input">
        </div>

        <div class="form-group">
            <label for="tasks">Tasks (one per line):</label>
            <textarea id="tasks" v-model="formData.tasksInput" required placeholder="Enter tasks, one per line" rows="5"
                class="form-textarea"></textarea>
        </div>

        <div class="form-group">
            <label for="completion">Completion Percentage:</label>
            <input type="number" id="completion" v-model="formData.completion_percentage" min="0" max="100" required
                class="form-input">
        </div>

        <button type="submit" class="submit-btn">Submit Project</button>
    </form>
</template>