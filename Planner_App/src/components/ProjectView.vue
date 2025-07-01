<script setup lang="ts">
import { onMounted, ref } from "vue";

interface Project {
    id: number,
    tasks: string[],
    name: string,
    completion_percentage: number
}

const FLASK_API_BASE_URL: string = "http://127.0.0.1:5000/api/projects";
const projects = ref<null | Project[]>(null);
const is_loading = ref<null | boolean>(null);
const error_msg = ref<string | null>(null);

const loadProjects = async (): Promise<void> => {
    is_loading.value = null;
    error_msg.value = null;
    projects.value = null;

    try {
        const response: Response = await fetch(FLASK_API_BASE_URL, {
            method: "GET"
        });

        if (!response.ok) {
            const errorBody = await response.text().catch(() => 'No error message available');
            throw new Error(`HTTP error! Status: ${response.status} - ${errorBody}`);
        }

        const loaded_projects: Project[] = await response.json() as Project[];
        projects.value = loaded_projects;
        console.log('Data fetched from API:', projects.value);


    } catch (error: any) {
        console.error('Error fetching data:', error);
        error_msg.value = `Failed to load data: ${error.message}`;
    } finally {
        // `finally` block runs regardless of success or failure, useful for cleanup like stopping loading.
        is_loading.value = false;
    }
}

onMounted(() => loadProjects());

</script>

<template>
    <p v-if="is_loading"> loading projects... </p>
    <h3 v-if="error_msg"> {{ error_msg }} </h3>

    <div class="project-view" v-if="projects && projects.length > 0">
        <div class="project-card" v-for="project in projects">
            <!-- <strong>ID:</strong> {{ project.id }}<br> -->
            <strong>Name:</strong> {{ project.name }}<br>
            <strong>Value:</strong> {{ String(project.completion_percentage) }}<br>
            <strong>Tasks Remaining:</strong><br>
            <ul v-if="project.tasks.length > 0">
                <li v-for="task in project.tasks">
                    {{ task }}
                </li>
            </ul>

            <p v-else> None Remaining</p>

        </div>
    </div>
</template>

<style scoped>
.project-view {
    display: flex;
    width: 100%;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: start;
    justify-content: space-between;
}

.project-card {
    width: 30%;
}
</style>